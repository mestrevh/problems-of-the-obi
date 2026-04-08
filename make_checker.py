import os
import csv

# Definições de pastas e arquivos
diretorio_base = 'output'
nome_arquivo_csv = 'check_questions.csv'

def criar_csv_checagem():
    # Verifica se a pasta 'output' existe no local onde o script está rodando
    if not os.path.exists(diretorio_base):
        print(f"Erro: O diretório '{diretorio_base}' não foi encontrado neste local.")
        return

    questoes = []

    # Lista tudo que tem dentro da pasta 'output'
    for item in os.listdir(diretorio_base):
        caminho_completo = os.path.join(diretorio_base, item)
        
        # Garante que vamos pegar apenas diretórios (ignorando arquivos como .txt, .zip, etc.)
        if os.path.isdir(caminho_completo):
            questoes.append(item)

    # Ordena os nomes das pastas em ordem alfabética para facilitar a organização
    questoes.sort()

    # Cria o arquivo CSV e escreve os dados
    with open(nome_arquivo_csv, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escreve o cabeçalho das colunas
        writer.writerow(['question', 'gabarito', 'img'])
        
        # Escreve cada diretório encontrado na coluna 'question' e deixa as outras em branco
        for questao in questoes:
            writer.writerow([questao, '', ''])

    print(f"Sucesso! O arquivo '{nome_arquivo_csv}' foi criado com {len(questoes)} questões listadas.")

if __name__ == "__main__":
    criar_csv_checagem()