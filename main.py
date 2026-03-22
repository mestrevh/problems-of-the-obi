import json
import os
from dotenv import load_dotenv
from pathlib import Path
from google import genai
from google.genai import types

# Carregar variáveis de ambiente
load_dotenv()

problemas_mapeados = []

def create_questions(pdfs_path):
    # 1. Inicializar o cliente com a NOVO SDK da Google
    client = genai.Client(api_key=os.getenv("GEMINI_API"))
    modelo_gemini = os.getenv("GEMINI_MODEL")

    # Corrigido: Procurar por todos os arquivos .pdf dentro da pasta data (e subpastas)

    if not pdfs_path:
        print("Nenhum arquivo PDF encontrado na pasta 'data'.")

    erros = []

    for pdf_path in pdfs_path:
        print(f"\n----------------------------------------")
        print(f"Processando arquivo: {pdf_path.name}")

        # 2. Fazer o upload do arquivo PDF (usando o caminho como string)
        print("Fazendo upload do PDF para a API...")
        arquivo_pdf = client.files.upload(file=str(pdf_path))

        # 3. Prompt de extração
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
                "difficulty": (Você tem 3 opções: Fácil, Médio, Difícil. Só pode escolher uma por exemplo "Difícil")
            }
        ]
        """

        print("Processando o documento com a LLM (isso pode levar um tempo maior por ser o documento todo)...")

        try:
            # 4. Fazer a chamada usando a nova estrutura do SDK
            response = client.models.generate_content(
                model=modelo_gemini,
                contents=[arquivo_pdf, prompt],
                config=types.GenerateContentConfig(
                    response_mime_type="application/json"
                )
            )

            # 5. Converter o texto retornado para uma lista Python (Array de dicionários)
            dados_json = json.loads(response.text)
            # Verifica quantos problemas foram extraídos
            quantidade_problemas = len(dados_json) if isinstance(
                dados_json, list) else 0
            print(
                f"Foram encontrados e extraídos {quantidade_problemas} problemas.")

            for output_json in dados_json:
                
                output_path = Path(f"output/{output_json['title']}")
                
                if output_path.exists():
                    arquivo_antigo = output_path / "problem.json"
                    
                    if arquivo_antigo.exists():
                        with open(arquivo_antigo, "r", encoding="utf-8") as f:
                            aux = json.load(f)

                        if aux['year'] != output_json['year']:
                            output_path = Path(f"output/{output_json['title']}_{output_json['year']}")
                    
                output_path.mkdir(parents=True, exist_ok=True)
                problemas_mapeados.append((output_json['year'], output_json['title']))
                
                with open(f"{str(output_path)}/problem.json", "w", encoding="utf-8") as f:
                    json.dump(output_json, f, indent=4, ensure_ascii=False)

                print(f"Sucesso! O arquivo '{output_json['title']}' foi gerado.")
            
        except json.JSONDecodeError:
            print("Erro: A API não retornou um JSON válido.")
            print("Resposta bruta:", response.text)
            erros.append(pdf_path)
        except Exception as e:
            print(f"Erro inesperado durante o processamento: {e}")
            erros.append(pdf_path)
        finally:
            # 7. Limpar o arquivo da API para não consumir armazenamento desnecessário
            try:
                client.files.delete(name=arquivo_pdf.name)
                print("Arquivo removido dos servidores da Google.")
            except:
                pass
    
    return erros


def atualizar_readme():
    print("\nAtualizando o README.md com base nos arquivos extraídos...")

    # 1. Agrupar os problemas por ano usando um dicionário
    problemas_por_ano = {}
    for ano, nome in problemas_mapeados:
        if ano not in problemas_por_ano:
            problemas_por_ano[ano] = []
        problemas_por_ano[ano].append(nome)

    secoes_anos_markdown = []

    # 2. Iterar sobre os anos agrupados (ordenando do mais recente para o mais antigo)
    for ano in sorted(problemas_por_ano.keys(), reverse=True):
        linhas_tabela = []

        for i, nome in enumerate(problemas_por_ano[ano], 1):
            # Exceção para o problema "Concurso"
            if nome == "Concurso":
                linhas_tabela.append(
                    f"| {i} | {nome} | ❌ | Inviável | ❌ Sem casos de teste |")
                continue

            # Verifica se a API conseguiu extrair o JSON
            caminho_json = Path(f"output/{nome}/problem.json")
            if caminho_json.exists():
                extracao = "OK"
                status = "Em andamento"
            else:
                extracao = "Pendente"
                status = "Pendente"

            linhas_tabela.append(
                f"| {i} | {nome} | {extracao} | Pendente | {status} |")

        tabela_markdown = "\n".join(linhas_tabela)

        # 3. Criar o bloco Markdown dinâmico para a edição atual (Ano)
        bloco_ano = f"""### OBI {ano}

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
{tabela_markdown}
"""
        secoes_anos_markdown.append(bloco_ano)

    # Junta todos os anos (2024, 2023, 2000, etc) separados por uma quebra de linha dupla
    todas_as_edicoes_markdown = "\n\n".join(secoes_anos_markdown)

    # 4. Construir o texto final do README
    readme_content = f"""# Database para o Experimento: OBI (Olimpíada Brasileira de Informática)

Este repositório cataloga e estrutura os problemas passados da OBI para a realização de experimentos e avaliação de LLMs em programação competitiva. 

O processo de construção desta base de dados é **híbrido**:
1. **Extração Automática:** Utilizamos um script em Python integrado à API do Google Gemini para ler os PDFs originais das provas e extrair os enunciados, restrições e regras em formato JSON (salvos em `output/<Nome do Problema>/problem.json`).
2. **Revisão Manual:** Como os casos de teste oficiais muitas vezes exigem formatação específica ou não estão totalmente disponíveis no texto do PDF, os mantenedores inserem os **casos de teste à mão** nos arquivos gerados.

**Fonte de Dados:** [Provas Passadas OBI - Unicamp](https://olimpiada.ic.unicamp.br/passadas/)

---

## Status Geral das Edições

| Ano | Status | Observação |
|:---:|:---|:---|
| **1999** | Descartado | Não possui gabarito para nenhuma questão. |
| **2000** | Em andamento | Iniciando mapeamento. |
| **2001 a 2023** | Pendente | Aguardando execução do script de extração. |
| **2024** | Mapeado | Extração via API concluída, inserção manual de testes em andamento. |

---

## Mapeamento por Edição

{todas_as_edicoes_markdown}
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("Sucesso! README.md atualizado de forma dinâmica para todos os anos inseridos.")

path_data = Path("data")
pdfs_path = list(path_data.rglob("*.pdf"))

while True:    
    pdfs_path = create_questions(pdfs_path=pdfs_path)
    
    if len(pdfs_path) == 0:
        break

# Chamar a função de atualização no final do script
atualizar_readme()