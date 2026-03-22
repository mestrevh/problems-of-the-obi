# Database para o Experimento: OBI (Olimpíada Brasileira de Informática)

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

### OBI 2024

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Ogro | OK | Pendente | ⏳ Em andamento |
| 2 | Bactérias | OK | Pendente | ⏳ Em andamento |
| 3 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 4 | Relógio | OK | Pendente | ⏳ Em andamento |
| 5 | Jogo da Vida | OK | Pendente | ⏳ Em andamento |
| 6 | Placas de Carro | OK | Pendente | ⏳ Em andamento |
| 7 | Avenida | OK | Pendente | ⏳ Em andamento |
| 8 | Alfabeto alienígena | OK | Pendente | ⏳ Em andamento |
| 9 | Atletismo | OK | Pendente | ⏳ Em andamento |
| 10 | Dança de Formatura | OK | Pendente | ⏳ Em andamento |
| 11 | Concatena Dígitos | OK | Pendente | ⏳ Em andamento |
| 12 | Cubo Preto | OK | Pendente | ⏳ Em andamento |
| 13 | Jogo do Poder | OK | Pendente | ⏳ Em andamento |
| 14 | Game Show | OK | Pendente | ⏳ Em andamento |
| 15 | Salada de Frutas | OK | Pendente | ⏳ Em andamento |
| 16 | Trio de Palitinhos | OK | Pendente | ⏳ Em andamento |
| 17 | Remove Dígitos | OK | Pendente | ⏳ Em andamento |
| 18 | Cadeado | Pendente | Pendente | ⏳ Pendente |
| 19 | Entrevista de emprego | Pendente | Pendente | ⏳ Pendente |
| 20 | Hotel Nlogônia | Pendente | Pendente | ⏳ Pendente |
| 21 | Musical | Pendente | Pendente | ⏳ Pendente |
| 22 | Brigadeiros | Pendente | Pendente | ⏳ Pendente |
| 23 | Construtora | Pendente | Pendente | ⏳ Pendente |
| 24 | Retas | Pendente | Pendente | ⏳ Pendente |
| 25 | Burocracia | Pendente | Pendente | ⏳ Pendente |
| 26 | Jogo de Pratos | Pendente | Pendente | ⏳ Pendente |