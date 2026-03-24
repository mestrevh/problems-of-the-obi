import os
import re
import json
import time
import shutil
import zipfile
import unicodedata
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai import types

# Carregar variáveis de ambiente
load_dotenv()

# Usar set em vez de list para evitar duplicações se o script repetir a extração de um PDF
problemas_mapeados = set()

# =====================================================================
# ETAPA 1: DOWNLOAD DOS CADERNOS (PDFs)
# =====================================================================


def baixar_cadernos_pdf():
    """Baixa todos os cadernos de prova em PDF do site da OBI para a pasta 'data'."""
    pasta_base = Path("data")
    pasta_base.mkdir(exist_ok=True)

    # Padrões de URL cobrindo todas as fases (incluindo as fases B)
    padroes_url = [
        "programacao/",
        "fase1/programacao/",
        "fase1b/programacao/",
        "fase2/programacao/",
        "fase2b/programacao/",
        "fase3/programacao/",
        "fase3b/programacao/"
    ]

    urls_ja_baixadas = set()

    print(f"\n{'='*40}")
    print("1. INICIANDO O DOWNLOAD DOS CADERNOS (PDFs)")
    print(f"{'='*40}")

    for ano in range(2000, 2025):
        print(f"\nBuscando PDFs do ano: {ano}")

        for padrao in padroes_url:
            url_pagina = f"https://olimpiada.ic.unicamp.br/passadas/OBI{ano}/{padrao}"

            try:
                response = requests.get(url_pagina, timeout=10)

                if response.status_code != 200:
                    continue

                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links:
                    href = link['href']

                    if href.lower().endswith('.pdf'):
                        url_completa = urljoin(url_pagina, href)

                        if url_completa in urls_ja_baixadas:
                            continue

                        nome_arquivo = href.split("/")[-1]
                        caminho_salvar = pasta_base / nome_arquivo

                        if caminho_salvar.exists():
                            print(f"  -> Já existe: {nome_arquivo}")
                            urls_ja_baixadas.add(url_completa)
                            continue

                        print(
                            f"  -> Baixando PDF: {nome_arquivo} ...", end=" ")

                        try:
                            resposta_pdf = requests.get(
                                url_completa, stream=True, timeout=15)
                            if resposta_pdf.status_code == 200:
                                with open(caminho_salvar, 'wb') as f:
                                    for chunk in resposta_pdf.iter_content(chunk_size=8192):
                                        f.write(chunk)
                                urls_ja_baixadas.add(url_completa)
                                print("OK!")
                            else:
                                print(f"ERRO {resposta_pdf.status_code}")
                        except Exception as e:
                            print(f"FALHA ({e})")

                        time.sleep(0.5)

            except requests.RequestException:
                continue

    print("\nDownload de PDFs finalizado!")

# =====================================================================
# ETAPA 2: EXTRAÇÃO DE QUESTÕES COM IA (GEMINI)
# =====================================================================


def create_questions(pdfs_path):
    client = genai.Client(api_key=os.getenv("GEMINI_API"))
    modelo_gemini = os.getenv("GEMINI_MODEL")

    if not pdfs_path:
        print("Nenhum arquivo PDF encontrado para processar.")
        return []

    erros = []

    for pdf_path in pdfs_path:
        print(f"\n----------------------------------------")
        print(f"Processando arquivo na LLM: {pdf_path.name}")

        print(pdf_path)
        print("Fazendo upload do PDF para a API...")
        arquivo_pdf = client.files.upload(file=str(pdf_path))

        prompt = """
        Você é um assistente especializado em extrair problemas de programação competitiva de PDFs da Olimpíada Brasileira de Informática (OBI).
        Leia o arquivo PDF em anexo e extraia os dados de TODOS os problemas que encontrar no documento.

        Retorne os dados ESTRITAMENTE no formato JSON abaixo, preenchendo com as informações do documento. 
        A sua resposta deve ser um ARRAY (lista) de objetos JSON, onde cada objeto representa um problema diferente.
        Não inclua nenhuma formatação markdown (como ```json) ou texto antes/depois do JSON.

        TEMPLATE ESPERADO:
        [
            {
                "title": "Nome do problema 1",
                "statement": "Texto completo da descrição do problema (história e regras). Mantenha as quebras de linha usando \\n",
                "input": "Texto da seção de Entrada",
                "output": "Texto da seção de Saída",
                "constraints": "Texto da seção de Restrições",
                "examples": [
                    {
                        "input": "exemplo de entrada 1",
                        "output": "exemplo de saída 1"
                    }
                ],
                "imgs": [],
                "rating": [int: pontuação subtarefa 0, int: pontuação subtarefa 1, ... , int: pontuação subtarefa n],
                "year": "2024",
                "level": "PJ",
                "period": "Fase 3",
                "difficulty": "Difícil [aqui só pode ter 3 valores únicos: Fácil, Médio ou Díficil]"
            }
        ]
        """

        print("Processando o documento com a LLM (isso pode levar um tempo maior por ser o documento todo)...")

        try:
            response = client.models.generate_content(
                model=modelo_gemini,
                contents=[arquivo_pdf, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            dados_json = json.loads(response.text)
            quantidade_problemas = len(dados_json) if isinstance(
                dados_json, list) else 0
            print(
                f"Foram encontrados e extraídos {quantidade_problemas} problemas.")

            for output_json in dados_json:
                titulo = output_json.get('title', 'Desconhecido')
                ano = output_json.get('year', 'Unknown')

                output_path = Path(f"output/{titulo}")

                # Resolução de conflitos de nome
                if output_path.exists():
                    arquivo_antigo = output_path / "problem.json"
                    if arquivo_antigo.exists():
                        with open(arquivo_antigo, "r", encoding="utf-8") as f:
                            aux = json.load(f)

                        if str(aux.get('year')) != str(ano):
                            titulo = f"{titulo}_{ano}"
                            output_path = Path(f"output/{titulo}")

                output_path.mkdir(parents=True, exist_ok=True)
                problemas_mapeados.add((ano, titulo))

                with open(f"{str(output_path)}/problem.json", "w", encoding="utf-8") as f:
                    json.dump(output_json, f, indent=4, ensure_ascii=False)

                print(f"Sucesso! O arquivo '{titulo}' foi gerado.")

        except json.JSONDecodeError:
            print("Erro: A API não retornou um JSON válido.")
            print("Resposta bruta:", response.text)
            erros.append(pdf_path)
        except Exception as e:
            print(f"Erro inesperado durante o processamento: {e}")
            erros.append(pdf_path)
        finally:
            try:
                client.files.delete(name=arquivo_pdf.name)
                print("Arquivo removido dos servidores da Google.")
            except:
                pass

    return erros

# =====================================================================
# ETAPA 3: DOWNLOAD DOS GABARITOS
# =====================================================================


def limpar_nome_arquivo(nome):
    """Remove caracteres inválidos para nomes de arquivos no Windows/Linux"""

    nome_limpo = re.sub(r'[\\/*?:"<>|]', "", nome)

    return nome_limpo.strip()


def baixar_gabaritos():

    pasta_base = "gabaritos_obi"
    os.makedirs(pasta_base, exist_ok=True)

    # Lista de possíveis caminhos (patterns) que a OBI usou ao longo dos anos
    padroes_url = [
        "programacao/",
        "programacao/cadernos/",
        "fase1/programacao/",
        "fase1/programacao/cadernos/",
        "fase1b/programacao/",
        "fase1b/programacao/cadernos/",
        "fase2/programacao/",
        "fase2/programacao/cadernos/",
        "fase2b/programacao/",
        "fase2b/programacao/cadernos/",
        "fase3/programacao/",
        "fase3/programacao/cadernos/",
        "fase3b/programacao/",
        "fase3b/programacao/cadernos/"
    ]

    # Conjunto para não baixar o mesmo arquivo duas vezes caso apareça em páginas diferentes

    urls_ja_baixadas = set()

    # Loop pelos anos (2000 a 2024)

    for ano in range(2000, 2025):
        print(f"\n{'='*40}")
        print(f"Buscando gabaritos do ano: {ano}")
        print(f"{'='*40}")
        pasta_ano = os.path.join(pasta_base, str(ano))
        os.makedirs(pasta_ano, exist_ok=True)
        encontrou_algo_no_ano = False

        # Testa cada variação de URL para o ano atual

        for padrao in padroes_url:
            url_pagina = f"https://olimpiada.ic.unicamp.br/passadas/OBI{ano}/{padrao}"
            try:
                response = requests.get(url_pagina, timeout=10)

                # Se a página não existir (404), pula para o próximo padrão

                if response.status_code != 200:
                    continue

                print(f"Página encontrada: {url_pagina}")

                soup = BeautifulSoup(response.text, 'html.parser')
                links = soup.find_all('a', href=True)

                for link in links:
                    href = link['href']

                    # Verifica se é um arquivo zip e se está na pasta de gabaritos

                    if href.endswith('.zip') and ('gabarito' in href.lower() or 'testes' in href.lower()):
                        url_completa = urljoin(url_pagina, href)

                        if url_completa in urls_ja_baixadas:
                            continue

                        # Pega o texto do link para ser o nome da questão (ex: "Entrevistas de emprego")
                        nome_questao = link.text.strip()

                        # Fallback: Se o link for uma imagem ou não tiver texto, usa o nome do arquivo original
                        if not nome_questao:
                            nome_questao = href.split(
                                "/")[-1].replace(".zip", "")

                        nome_arquivo_final = f"{limpar_nome_arquivo(nome_questao)}.zip"
                        caminho_salvar = os.path.join(
                            pasta_ano, nome_arquivo_final)

                        print(f"  -> Baixando: {nome_questao} ...", end=" ")
                        try:
                            resposta_zip = requests.get(
                                url_completa, stream=True, timeout=15)

                            if resposta_zip.status_code == 200:
                                with open(caminho_salvar, 'wb') as f:
                                    for chunk in resposta_zip.iter_content(chunk_size=8192):
                                        f.write(chunk)

                                urls_ja_baixadas.add(url_completa)
                                encontrou_algo_no_ano = True

                                print("OK!")

                            else:
                                print(f"ERRO {resposta_zip.status_code}")

                        except Exception as e:
                            print(f"FALHA ({e})")

                        # Pequena pausa para não sobrecarregar o servidor da Unicamp
                        time.sleep(0.5)

            except requests.RequestException:
                # Ignora erros de conexão e tenta a próxima URL
                continue

        if not encontrou_algo_no_ano:

            print(
                f"Nenhum gabarito em .zip encontrado para {ano} nas URLs testadas.")

    print("\nProcesso finalizado com sucesso! Verifique a pasta 'gabaritos_obi'.")


# =====================================================================
# ETAPA 4: EXTRAÇÃO E ORGANIZAÇÃO DOS GABARITOS
# =====================================================================
def normalizar_nome(nome):
    nome_sem_acento = ''.join(c for c in unicodedata.normalize('NFD', nome)
                              if unicodedata.category(c) != 'Mn')
    return nome_sem_acento.lower().replace(' ', '').replace('-', '').replace('_', '').strip()


def organizar_test_cases():
    print(f"\n{'='*40}")
    print("4. DESCOMPACTANDO GABARITOS NAS PASTAS DE OUTPUT")
    print(f"{'='*40}")

    path_output = Path("output")
    path_gabaritos = Path("gabaritos_obi")

    if not path_output.exists() or not path_gabaritos.exists():
        print("Pastas necessárias não encontradas. Pulando etapa.")
        return

    pastas_output = {}
    for pasta in path_output.iterdir():
        if pasta.is_dir():
            pastas_output[normalizar_nome(pasta.name)] = pasta

    zips_processados = 0
    zips_sem_match = []

    for arquivo_zip in path_gabaritos.rglob("*.zip"):
        ano_gabarito = arquivo_zip.parent.name
        nome_zip = arquivo_zip.stem

        nome_norm_simples = normalizar_nome(nome_zip)
        nome_norm_com_ano = normalizar_nome(f"{nome_zip}_{ano_gabarito}")

        pasta_destino = pastas_output.get(
            nome_norm_com_ano) or pastas_output.get(nome_norm_simples)

        if pasta_destino:
            test_cases_dir = pasta_destino / "test_cases"
            test_cases_dir.mkdir(exist_ok=True)

            # Checa se a pasta está vazia antes de descompactar para não extrair duas vezes
            if not any(test_cases_dir.iterdir()):
                try:
                    with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
                        zip_ref.extractall(test_cases_dir)

                    print(
                        f"  -> Extrato com sucesso: {pasta_destino.name}/test_cases")
                    arquivo_zip.unlink()  # Deleta o zip limpo
                    zips_processados += 1
                except zipfile.BadZipFile:
                    print(f"  -> ERRO: ZIP corrompido: {arquivo_zip.name}")
        else:
            zips_sem_match.append(f"{ano_gabarito} - {nome_zip}.zip")

    for pasta_ano in path_gabaritos.iterdir():
        if pasta_ano.is_dir() and not any(pasta_ano.iterdir()):
            pasta_ano.rmdir()

# =====================================================================
# ETAPA 5: LIMPEZA DOS TEST CASES
# =====================================================================


def limpar_pastas_test_cases():
    print(f"\n{'='*40}")
    print("5. LIMPANDO E REESTRUTURANDO TEST CASES")
    print(f"{'='*40}")

    path_output = Path("output")
    if not path_output.exists():
        return

    problemas_processados = 0

    for pasta_problema in path_output.iterdir():
        if not pasta_problema.is_dir():
            continue

        test_cases_dir = pasta_problema / "test_cases"
        if not test_cases_dir.exists():
            continue

        pastas_numeradas = []
        for item in test_cases_dir.rglob("*"):
            if item.is_dir() and item.name.isdigit():
                pastas_numeradas.append(item)

        quantidade_movida = 0
        for pasta in pastas_numeradas:
            destino = test_cases_dir / pasta.name
            if pasta != destino:
                if destino.exists():
                    shutil.rmtree(destino)
                shutil.move(str(pasta), str(destino))
                quantidade_movida += 1

        for item in test_cases_dir.iterdir():
            if item.is_dir():
                if not item.name.isdigit():
                    shutil.rmtree(item)
            else:
                # NOVO: Protege o carimbo para ele não ser deletado na limpeza
                if item.name != ".auto":
                    item.unlink()

        if quantidade_movida > 0 or pastas_numeradas:
            print(
                f"[{pasta_problema.name}] {len(pastas_numeradas)} casos limpos mantidos.")
            problemas_processados += 1

# =====================================================================
# ETAPA 5.5: REMOÇÃO DE QUESTÕES SEM TEST CASES
# =====================================================================


def remover_questoes_sem_testes():
    print(f"\n{'='*40}")
    print("5.5. REMOVENDO QUESTÕES SEM CASOS DE TESTE")
    print(f"{'='*40}")

    path_output = Path("output")
    if not path_output.exists():
        print("Pasta 'output' não encontrada.")
        return

    questoes_removidas = 0
    global problemas_mapeados  # Usamos global para atualizar a lista do README

    # Usamos list() para não alterar o iterador enquanto apagamos pastas
    for pasta_problema in list(path_output.iterdir()):
        if not pasta_problema.is_dir():
            continue

        test_cases_dir = pasta_problema / "test_cases"

        # Checa se a pasta test_cases existe e se possui algum arquivo/pasta dentro
        tem_testes = test_cases_dir.exists() and any(test_cases_dir.iterdir()) and len(list(test_cases_dir.rglob("*"))) > 1

        if not tem_testes:
            print(
                f" ❌ Removendo: '{pasta_problema.name}' (Sem casos de teste)")
            # Deleta a pasta e todo o seu conteúdo
            shutil.rmtree(pasta_problema)
            questoes_removidas += 1

            # Remove da lista global para não aparecer no README
            problemas_mapeados = {
                (ano, titulo) for ano, titulo in problemas_mapeados if titulo != pasta_problema.name}

    print(
        f"\nTotal de questões removidas por falta de testes: {questoes_removidas}")

# =====================================================================
# ETAPA 6: ATUALIZAÇÃO DO README
# =====================================================================


def atualizar_readme():
    print(f"\n{'='*40}")
    print("6. ATUALIZANDO O README.MD")
    print(f"{'='*40}")

    problemas_por_ano = {}
    for ano, nome in problemas_mapeados:
        if ano not in problemas_por_ano:
            problemas_por_ano[ano] = []
        if nome not in problemas_por_ano[ano]:
            problemas_por_ano[ano].append(nome)

    secoes_anos_markdown = []

    for ano in sorted(problemas_por_ano.keys(), reverse=True):
        linhas_tabela = []

        for i, nome in enumerate(problemas_por_ano[ano], 1):
            if nome == "Concurso":
                linhas_tabela.append(
                    f"| {i} | {nome} | ❌ | Inviável | ❌ Sem casos de teste |")
                continue

            caminho_json = Path(f"output/{nome}/problem.json")
            caminho_testes = Path(f"output/{nome}/test_cases")

            testes_status = "Pendente"
            status = "Pendente"

            if caminho_json.exists():
                extracao = "OK"
                status = "⚠️ Aguardando Testes"

                if caminho_testes.exists():
                    # Verifica o que tem na pasta ignorando o nosso marcador
                    conteudo = [f for f in caminho_testes.iterdir()
                                if f.name != ".auto"]

                    if len(conteudo) > 0:
                        # Se o marcador estiver lá, foi o script. Se não, foi você.
                        if (caminho_testes / ".auto").exists():
                            testes_status = "🤖 Auto"
                        else:
                            testes_status = "🧑‍💻 Manual"

                        status = "✅ Concluído"

            linhas_tabela.append(
                f"| {i} | {nome} | {extracao} | {testes_status} | {status} |")

        tabela_markdown = "\n".join(linhas_tabela)

        bloco_ano = f"""### OBI {ano}

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que a LLM extraiu o JSON com sucesso.
* **Testes**: `[🤖 Auto]` baixado da OBI, `[🧑‍💻 Manual]` inserido manualmente, `[Pendente]` falta fazer.

| # | Problema | Extração (API) | Testes | Status Final |
|:---:|:---|:---:|:---:|:---:|
{tabela_markdown}
"""
        secoes_anos_markdown.append(bloco_ano)

    todas_as_edicoes_markdown = "\n\n".join(secoes_anos_markdown)

    readme_content = f"""# Database para o Experimento: OBI (Olimpíada Brasileira de Informática)

Este repositório cataloga e estrutura os problemas passados da OBI para a realização de experimentos e avaliação de LLMs em programação competitiva. 

### ⚙️ Pipeline de Automação

1. 📄 **Download dos Cadernos:** Baixar provas passadas no formato PDF.
2. 🤖 **Extração via LLM:** Processar os PDFs e extrair os dados das questões em formato JSON.
3. 📦 **Download dos Gabaritos:** Baixar todos os arquivos de casos de teste em `.zip`.
4. 📂 **Organização:** Criar as pastas `test_cases` e associar os gabaritos às questões corretas.
5. 🧹 **Limpeza de Dados:** Remover pastas vazias, arquivos desnecessários e padronizar.
6. 📝 **Atualização do README:** Atualizar o documento principal detectando automaticamente o progresso. 

**Fonte de Dados:** [Provas Passadas OBI - Unicamp](https://olimpiada.ic.unicamp.br/passadas/)

---

## Mapeamento por Edição

{todas_as_edicoes_markdown}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("Sucesso! README.md atualizado.")


# =====================================================================
# INICIALIZAÇÃO DA PIPELINE
# =====================================================================
if __name__ == "__main__":
    print("\n🚀 INICIANDO PIPELINE DE AUTOMAÇÃO DA OBI 🚀\n")

    # Passo 1: Baixar PDFs
    #baixar_cadernos_pdf()

    # Passo 2: Mandar para LLM
    #print(f"\n{'='*40}")
    #print("2. EXTRAÇÃO DE DADOS (API GEMINI)")
    #print(f"{'='*40}")
    #path_data = Path("data")
    #pdfs_path = list(path_data.rglob("*.pdf"))
    
    #while True:    
    #    pdfs_path = create_questions(pdfs_path=pdfs_path)
    #    if len(pdfs_path) == 0:
    #        break

    # Passo 3: Baixar ZIPs de gabaritos
    baixar_gabaritos()

    # Passo 4: Cruzar ZIPs com Pastas Output
    organizar_test_cases()

    # Passo 5: Limpar estrutura dos ZIPs
    limpar_pastas_test_cases()

    # Passo 5.5: NOVO - Remover questões sem testes válidos
    remover_questoes_sem_testes()

    # Passo 6: Atualizar documento README com status atualizado
    #atualizar_readme()

    print("\n🎉 PIPELINE FINALIZADA COM SUCESSO! 🎉")
