# Database para o Experimento: OBI (Olimpíada Brasileira de Informática)

Este repositório cataloga e estrutura os problemas passados da OBI para a realização de experimentos e avaliação de LLMs em programação competitiva. 

### ⚙️ Pipeline de Automação

1. 📄 **Download dos Cadernos:** Baixar provas passadas no formato PDF.
2. 🤖 **Extração via LLM:** Processar os PDFs e extrair os dados das questões em formato JSON.
3. 📦 **Download dos Gabaritos:** Baixar todos os arquivos de casos de teste em `.zip`.
4. 📂 **Organização:** Criar as pastas `test_cases` e associar os gabaritos às questões corretas.
5. 🧹 **Limpeza de Dados:** Remover pastas vazias, arquivos desnecessários e padronizar.
6. 📝 **Atualização do README:** Atualizar o documento principal detectando automaticamente o progresso. 

**Fonte de Dados:** [Provas Passadas OBI - Unicamp](https://olimpiada.ic.unicamp.br/passadas/)

## Resultados

Questões estão em `output`

- **Custo da extração:** aproximadamente R$ 100,00
- **Modelo utilizado:** Gemini 3.1 pro preview 
- **Total de questões extraídos:** 441
- **Quantidade de questões sem casos de teste:** 31
- **Quantidade de questões com casos de teste:** 412
- **Quantidade de questões com imagens:** 159
- **Quantidade de questões sem imagens:** 282
- **Estado atual:** `dataset-questions-obi.zip`, `provas-obi.zip` e `gabaritos-obi.zip`