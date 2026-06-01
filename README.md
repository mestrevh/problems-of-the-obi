# Banco de Problemas OBI — Repositório para Experimentos e Avaliação

Este repositório centraliza, padroniza e disponibiliza problemas da Olimpíada Brasileira de Informática (OBI) com o objetivo de suportar experimentos em recuperação, avaliação e geração automática por modelos de linguagem e sistemas de correção automática.

**Resumo:** coletamos provas públicas, extraímos metadados e enunciados em JSON, associamos casos de teste quando disponíveis e organizamos o material em uma estrutura reprodutível para pesquisa.

**Fonte de dados:** [Provas Passadas OBI - Unicamp](https://olimpiada.ic.unicamp.br/passadas/)

**Visão geral do conteúdo**
- Problemas processados e exportados em JSON na pasta `output`.
- Gabaritos e casos de teste organizados (quando disponíveis) em arquivos ZIP vinculados ao conjunto.
- Scripts auxiliares para processamento e verificação em `main.py` e `check_questions.py`.

**Objetivos do repositório**
- Fornecer um dataset de problemas da OBI, anotado e testável, para avaliação de LLMs e ferramentas de correção automática.
- Tornar reproduzível o pipeline de extração e organização das provas.
- Facilitar estudos comparativos, benchmarks e análises métricas sobre desempenho de modelos em problemas de programação competitiva.

## Pipeline de Automação
O processo automatizado adotado no projeto segue etapas claras e reprodutíveis:

1. Download das provas em PDF a partir das fontes públicas.
2. Extração dos enunciados e metadados via pipeline automatizado (uso de OCR quando necessário e pós-processamento por LLMs para estruturar JSON).
3. Download e associação dos gabaritos e casos de teste (.zip) às questões correspondentes.
4. Organização da saída em diretórios por problema dentro de `output/` (cada problema contém um arquivo `problem.json` com enunciado, entradas, saídas e metadados).
5. Limpeza e normalização (remoção de duplicatas, padronização de campos, verificação mínima de consistência).
6. Verificação manual pontual (amostragem e correção de erros críticos, especialmente para imagens e casos de teste faltantes).

## Estatísticas e Resultados (resumo)
- Total de questões extraídas: 493
- Com casos de teste: 468
- Sem casos de teste: 25
- Com imagens: 188
- Sem imagens: 305
- Custo aproximado da extração: R$ 100,00
- Modelo inicial usado para extração: Gemini 3.1 (etapa de prova-conceitual)

Estado atual dos artefatos: conjuntos gerados estão empacotados como `dataset-questions-obi.zip`, `provas-obi.zip` e `gabaritos-obi.zip`.

## Estrutura do repositório
- `output/` — diretório com subpastas por problema contendo `problem.json`, recursos e gabaritos quando presentes.
- `gabaritos_obi/` — repositório local dos gabaritos originais baixados e organizados por ano.
- `data/` — arquivos de apoio e exemplos de entrada.
- `main.py` — script principal de orquestração do pipeline.
- `check_questions.py` e `check_questions.csv` — ferramentas e logs para verificação e controle de qualidade.

## Como usar (rápido)
1. Instale dependências:

```bash
pip install -r requirements.txt
```

2. Executar verificação básica:

```bash
python check_questions.py
```

3. Executar o pipeline de extração/parsing (quando disponível e configurado):

```bash
python main.py
```

Observação: alguns passos do pipeline requerem arquivos ZIP externos (`provas-obi.zip`, `gabaritos-obi.zip`) e/ou credenciais para baixar fontes; leia os scripts para detalhes de configuração.

## Observações metodológicas (para artigo)
- Extração automatizada combina OCR (quando necessário) e pós-processamento por LLMs para estruturação em JSON — descreva as heurísticas adotadas ao reproduzir ou estender o trabalho.
- A associação de casos de teste foi parcialmente automatizada e complementada por verificação manual para garantir correspondência entre enunciados e gabaritos.
- Limitações conhecidas: erros de OCR em imagens complexas; casos de teste faltantes em algumas questões; ambiguidade em enunciados que exigiram intervenção humana.

## Disponibilidade e uso dos dados
- Os artefatos empacotados (ZIPs) estão listados na raiz do projeto e podem ser usados para experimentos sob as mesmas condições da fonte pública. Verifique licenças das provas originais antes de redistribuir.

## Contato
Para dúvidas, colaboração ou solicitações de dados adicionais, abra uma issue ou entre em contato com o mantenedor do repositório.

---
Versão resumida: este repositório é um banco de problemas da OBI, organizado para pesquisa e escrita de artigos sobre avaliação de modelos em tarefas de programação competitiva.