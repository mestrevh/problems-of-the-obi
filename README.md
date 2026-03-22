# Database para o Experimento: OBI (Olimpíada Brasileira de Informática)

Este repositório cataloga e estrutura os problemas passados da OBI para a realização de experimentos e avaliação de LLMs em programação competitiva. 

O processo de construção desta base de dados é **híbrido**:
1. **Extração Automática:** Utilizamos um script em Python integrado à API do Google Gemini para ler os PDFs originais das provas e extrair os enunciados, restrições e regras em formato JSON (salvos em `output/<Nome do Problema>/problem.json`), além disso, o modelo que utilizamos foi o gemini-2.5-pro.
2. **Revisão Manual:** Como os casos de teste oficiais muitas vezes exigem formatação específica ou não estão totalmente disponíveis no texto do PDF, os mantenedores inserem os **casos de teste à mão** nos arquivos 

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
| 1 | Cadeado | OK | Pendente | Em andamento |
| 2 | Amigos | OK | Pendente | Em andamento |
| 3 | Entrevistas de emprego | OK | Pendente | Em andamento |
| 4 | Hotel Nlogônia | OK | Pendente | Em andamento |
| 5 | Avenida | OK | Pendente | Em andamento |
| 6 | Alfabeto Alienígena | OK | Pendente | Em andamento |
| 7 | Dança de Formatura | OK | Pendente | Em andamento |
| 8 | Concatena Dígitos | OK | Pendente | Em andamento |
| 9 | Cubo Preto | OK | Pendente | Em andamento |
| 10 | Alfabeto Alienígena | OK | Pendente | Em andamento |
| 11 | Concatena Dígitos | OK | Pendente | Em andamento |
| 12 | Jogo do Poder | OK | Pendente | Em andamento |
| 13 | Musical | OK | Pendente | Em andamento |
| 14 | Entrevistas de emprego | OK | Pendente | Em andamento |
| 15 | Hotel Nlogônia | OK | Pendente | Em andamento |
| 16 | Brigadeiros | OK | Pendente | Em andamento |
| 17 | Cubo Preto | OK | Pendente | Em andamento |
| 18 | Alfabeto Alienígena | OK | Pendente | Em andamento |
| 19 | Dança de Formatura | OK | Pendente | Em andamento |
| 20 | Jogo do Poder | OK | Pendente | Em andamento |
| 21 | Brigadeiros | OK | Pendente | Em andamento |
| 22 | Construtora | OK | Pendente | Em andamento |
| 23 | Retas | OK | Pendente | Em andamento |
| 24 | Burocracia | OK | Pendente | Em andamento |
| 25 | Jogo de Pratos | OK | Pendente | Em andamento |
| 26 | Game Show | OK | Pendente | Em andamento |
| 27 | Salada de Frutas | OK | Pendente | Em andamento |
| 28 | Trio de Palitinhos | OK | Pendente | Em andamento |
| 29 | Remove Dígitos | OK | Pendente | Em andamento |
| 30 | Avenida | OK | Pendente | Em andamento |
| 31 | Alfabeto alienígena | OK | Pendente | Em andamento |
| 32 | Atletismo | OK | Pendente | Em andamento |
| 33 | Brigadeiros | OK | Pendente | Em andamento |
| 34 | Construtora | OK | Pendente | Em andamento |
| 35 | Retas | OK | Pendente | Em andamento |
| 36 | Burocracia | OK | Pendente | Em andamento |
| 37 | Jogo de Pratos | OK | Pendente | Em andamento |


### OBI 2023

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Ogro | OK | Pendente | Em andamento |
| 2 | Relógio | OK | Pendente | Em andamento |
| 3 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 4 | Jogo da Vida | OK | Pendente | Em andamento |
| 5 | Código de compressão | OK | Pendente | Em andamento |
| 6 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 7 | Intervalo Distinto | OK | Pendente | Em andamento |
| 8 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 9 | Prefixo | OK | Pendente | Em andamento |
| 10 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 11 | Intervalo Distinto | OK | Pendente | Em andamento |
| 12 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 13 | Pirâmide | OK | Pendente | Em andamento |
| 14 | Transportes | OK | Pendente | Em andamento |
| 15 | Oficina Mecânica | OK | Pendente | Em andamento |
| 16 | Trio de Bonecas | OK | Pendente | Em andamento |
| 17 | Fast-Food | OK | Pendente | Em andamento |
| 18 | Pizza da OВІ | OK | Pendente | Em andamento |
| 19 | Código de Compressão | OK | Pendente | Em andamento |
| 20 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 21 | Cabo de guerra | OK | Pendente | Em andamento |
| 22 | Metrônibus | OK | Pendente | Em andamento |
| 23 | Dominó Nlogônico | OK | Pendente | Em andamento |
| 24 | Oficina Mecânica | OK | Pendente | Em andamento |
| 25 | Código de compressão | OK | Pendente | Em andamento |
| 26 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 27 | Intervalo Distinto | OK | Pendente | Em andamento |
| 28 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 29 | Ogro | OK | Pendente | Em andamento |
| 30 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 31 | Placas de Carro | OK | Pendente | Em andamento |
| 32 | Jogo da Vida | OK | Pendente | Em andamento |
| 33 | Prêmio | OK | Pendente | Em andamento |
| 34 | Epidemia | OK | Pendente | Em andamento |
| 35 | Chinelos | OK | Pendente | Em andamento |
| 36 | Prefixo | OK | Pendente | Em andamento |
| 37 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 38 | Intervalo Distinto | OK | Pendente | Em andamento |
| 39 | VAR | OK | Pendente | Em andamento |
| 40 | Estoque | OK | Pendente | Em andamento |
| 41 | Subsequência | OK | Pendente | Em andamento |
| 42 | Ogro | OK | Pendente | Em andamento |
| 43 | Relógio | OK | Pendente | Em andamento |
| 44 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 45 | Ogro | OK | Pendente | Em andamento |
| 46 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 47 | Bactérias | OK | Pendente | Em andamento |
| 48 | Contas a pagar | OK | Pendente | Em andamento |
| 49 | Leilão | OK | Pendente | Em andamento |
| 50 | Estoque | OK | Pendente | Em andamento |
| 51 | Toupeira | OK | Pendente | Em andamento |
| 52 | Contas a pagar | OK | Pendente | Em andamento |
| 53 | Estoque | OK | Pendente | Em andamento |
| 54 | Subsequência | OK | Pendente | Em andamento |
| 55 | Sr. Toupeira | OK | Pendente | Em andamento |
| 56 | Cabo de guerra | OK | Pendente | Em andamento |
| 57 | Tesouro | OK | Pendente | Em andamento |
| 58 | Metrônibus | OK | Pendente | Em andamento |
| 59 | Oficina Mecânica | OK | Pendente | Em andamento |
| 60 | Prefixo | OK | Pendente | Em andamento |
| 61 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 62 | Intervalo Distinto | OK | Pendente | Em andamento |
| 63 | Pirâmide | OK | Pendente | Em andamento |
| 64 | Transportes | OK | Pendente | Em andamento |
| 65 | Oficina Mecânica | OK | Pendente | Em andamento |
| 66 | Trio de Bonecas | OK | Pendente | Em andamento |
| 67 | Fast-Food | OK | Pendente | Em andamento |
| 68 | Pizza da OBI | OK | Pendente | Em andamento |
| 69 | Código de Compressão | OK | Pendente | Em andamento |
| 70 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 71 | Prefixo | OK | Pendente | Em andamento |
| 72 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 73 | Intervalo Distinto | OK | Pendente | Em andamento |
| 74 | Barcos da Nlogônia | OK | Pendente | Em andamento |


### OBI 2022

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Restaurante de pizza | OK | Pendente | Em andamento |
| 2 | Carro elétrico | OK | Pendente | Em andamento |
| 3 | Dígitos | OK | Pendente | Em andamento |
| 4 | Pilhas de moedas | OK | Pendente | Em andamento |
| 5 | Caravana | OK | Pendente | Em andamento |
| 6 | Dígitos | OK | Pendente | Em andamento |
| 7 | Quadrado | OK | Pendente | Em andamento |
| 8 | Dona Minhoca | OK | Pendente | Em andamento |
| 9 | Construção de Rodovia | OK | Pendente | Em andamento |
| 10 | Cinema | OK | Pendente | Em andamento |
| 11 | Hotel | OK | Pendente | Em andamento |
| 12 | Quadrado Mágico | OK | Pendente | Em andamento |
| 13 | Caravana | OK | Pendente | Em andamento |
| 14 | Dígitos | OK | Pendente | Em andamento |
| 15 | Pilhas de moedas | OK | Pendente | Em andamento |
| 16 | Dona Minhoca | OK | Pendente | Em andamento |
| 17 | Rodovia | OK | Pendente | Em andamento |
| 18 | Hotel | OK | Pendente | Em andamento |
| 19 | Maior valor | OK | Pendente | Em andamento |
| 20 | Quadrado Mágico | OK | Pendente | Em andamento |
| 21 | Chuva | OK | Pendente | Em andamento |
| 22 | Cinema | OK | Pendente | Em andamento |
| 23 | Hotel | OK | Pendente | Em andamento |
| 24 | Show | OK | Pendente | Em andamento |
| 25 | Hotel | OK | Pendente | Em andamento |
| 26 | Bombom | OK | Pendente | Em andamento |
| 27 | Maior valor | OK | Pendente | Em andamento |
| 28 | Chuva | OK | Pendente | Em andamento |
| 29 | Tanque de combustível | OK | Pendente | Em andamento |
| 30 | Pirâmide | OK | Pendente | Em andamento |
| 31 | Câmeras | OK | Pendente | Em andamento |
| 32 | Tanque de combustível | OK | Pendente | Em andamento |
| 33 | Pirâmide | OK | Pendente | Em andamento |
| 34 | Subcadeias | OK | Pendente | Em andamento |
| 35 | Viagem | OK | Pendente | Em andamento |
| 36 | Troféu | OK | Pendente | Em andamento |
| 37 | Câmeras | OK | Pendente | Em andamento |
| 38 | Subcadeias | OK | Pendente | Em andamento |
| 39 | Viagem | OK | Pendente | Em andamento |
| 40 | Jogo | OK | Pendente | Em andamento |
| 41 | Teste de redação | OK | Pendente | Em andamento |
| 42 | Carro elétrico | OK | Pendente | Em andamento |
| 43 | Dígitos | OK | Pendente | Em andamento |
| 44 | Troféu | OK | Pendente | Em andamento |
| 45 | Caminho | OK | Pendente | Em andamento |
| 46 | Pirâmide | OK | Pendente | Em andamento |


### OBI 2021

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Ogro | OK | Pendente | Em andamento |
| 2 | Casamento de inteiros | OK | Pendente | Em andamento |
| 3 | Sr. Sapo | OK | Pendente | Em andamento |
| 4 | Plano de estacionamento | OK | Pendente | Em andamento |
| 5 | Recorde | OK | Pendente | Em andamento |
| 6 | Potência | OK | Pendente | Em andamento |
| 7 | Cálculo rápido | OK | Pendente | Em andamento |
| 8 | Lista palíndroma | OK | Pendente | Em andamento |
| 9 | Duplas de tênis | OK | Pendente | Em andamento |
| 10 | Retângulo | OK | Pendente | Em andamento |
| 11 | Robô | OK | Pendente | Em andamento |
| 12 | Média e mediana | OK | Pendente | Em andamento |
| 13 | Cálculo rápido | OK | Pendente | Em andamento |
| 14 | Lista palíndroma | OK | Pendente | Em andamento |
| 15 | Poligrama | OK | Pendente | Em andamento |
| 16 | Senha da Vó Zinha | OK | Pendente | Em andamento |
| 17 | Média ou mediana | OK | Pendente | Em andamento |
| 18 | Passatempo | OK | Pendente | Em andamento |
| 19 | Sanduíche | OK | Pendente | Em andamento |
| 20 | Retângulo | OK | Pendente | Em andamento |
| 21 | Idade de Camila | OK | Pendente | Em andamento |
| 22 | Zero para cancelar | OK | Pendente | Em andamento |
| 23 | Tempo de resposta | OK | Pendente | Em andamento |
| 24 | Cifra da Nlogônia | OK | Pendente | Em andamento |
| 25 | Mínimo e máximo | OK | Pendente | Em andamento |
| 26 | Lista palíndroma | OK | Pendente | Em andamento |
| 27 | Poligrama | OK | Pendente | Em andamento |
| 28 | Senha da Vó Zinha | OK | Pendente | Em andamento |
| 29 | Ogro | OK | Pendente | Em andamento |
| 30 | Teclado | OK | Pendente | Em andamento |
| 31 | Falha de segurança | OK | Pendente | Em andamento |
| 32 | Festa olímpica | OK | Pendente | Em andamento |
| 33 | Dona Minhoca | OK | Pendente | Em andamento |
| 34 | Casamento de inteiros | OK | Pendente | Em andamento |
| 35 | Sr. Sapo | OK | Pendente | Em andamento |
| 36 | Festa olímpica | OK | Pendente | Em andamento |
| 37 | Plano de estacionamento | OK | Pendente | Em andamento |
| 38 | Recorde | OK | Pendente | Em andamento |
| 39 | Anagrama | OK | Pendente | Em andamento |
| 40 | Potência | OK | Pendente | Em andamento |
| 41 | Pesquisa de preços | OK | Pendente | Em andamento |
| 42 | Casamento de inteiros | OK | Pendente | Em andamento |
| 43 | Cubo e quadrado | OK | Pendente | Em andamento |
| 44 | Festa olímpica | OK | Pendente | Em andamento |
| 45 | Falha de segurança | OK | Pendente | Em andamento |
| 46 | Dona Minhoca | OK | Pendente | Em andamento |
| 47 | Dupla de tênis | OK | Pendente | Em andamento |
| 48 | Passatempo | OK | Pendente | Em andamento |
| 49 | Sanduíche | OK | Pendente | Em andamento |
| 50 | Retângulo | OK | Pendente | Em andamento |
| 51 | Idade de Camila | OK | Pendente | Em andamento |
| 52 | Plano de Internet | OK | Pendente | Em andamento |
| 53 | Torneio de tênis | OK | Pendente | Em andamento |
| 54 | Duplas de tênis | OK | Pendente | Em andamento |
| 55 | Pangrama | OK | Pendente | Em andamento |
| 56 | Robô | OK | Pendente | Em andamento |
| 57 | Média e mediana | OK | Pendente | Em andamento |
| 58 | Torneio de tênis | OK | Pendente | Em andamento |
| 59 | Zero para cancelar | OK | Pendente | Em andamento |
| 60 | Tempo de resposta | OK | Pendente | Em andamento |
| 61 | Baralho | OK | Pendente | Em andamento |
| 62 | Torneio de tênis | OK | Pendente | Em andamento |
| 63 | Tempo de resposta | OK | Pendente | Em andamento |
| 64 | Zero para cancelar | OK | Pendente | Em andamento |


### OBI 2020

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Irmãos | OK | Pendente | Em andamento |
| 2 | Três por Dois | OK | Pendente | Em andamento |
| 3 | Camisetas da Olimpíada | OK | Pendente | Em andamento |
| 4 | Ralouim | OK | Pendente | Em andamento |
| 5 | Aplicativo de Calorias | OK | Pendente | Em andamento |
| 6 | Cobertura para Celular | OK | Pendente | Em andamento |
| 7 | Atlanta | OK | Pendente | Em andamento |
| 8 | Torre de Dados | OK | Pendente | Em andamento |
| 9 | Piloto Automático | OK | Pendente | Em andamento |
| 10 | Fissura Perigosa | OK | Pendente | Em andamento |
| 11 | Pandemia | OK | Pendente | Em andamento |
| 12 | Relógio de Atleta | OK | Pendente | Em andamento |
| 13 | Divisão do Tesouro | OK | Pendente | Em andamento |
| 14 | Camisetas da Olimpíada | OK | Pendente | Em andamento |
| 15 | Torre de dados | OK | Pendente | Em andamento |
| 16 | Candidatas | OK | Pendente | Em andamento |
| 17 | Aplicativo de calorias | OK | Pendente | Em andamento |
| 18 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 19 | Trem da mina | OK | Pendente | Em andamento |
| 20 | Dona Formiga | OK | Pendente | Em andamento |
| 21 | Fotografia | OK | Pendente | Em andamento |
| 22 | Caixeiro Viajante | OK | Pendente | Em andamento |
| 23 | Estrada | OK | Pendente | Em andamento |
| 24 | Irmãos | OK | Pendente | Em andamento |
| 25 | Garamana | OK | Pendente | Em andamento |
| 26 | Camisetas da Olimpíada | OK | Pendente | Em andamento |
| 27 | Música para Todos | OK | Pendente | Em andamento |
| 28 | Dona Formiga | OK | Pendente | Em andamento |
| 29 | Estrada | OK | Pendente | Em andamento |
| 30 | Dona Lesma | OK | Pendente | Em andamento |
| 31 | Acelerador de Partículas | OK | Pendente | Em andamento |
| 32 | Promoção de Primeira | OK | Pendente | Em andamento |
| 33 | Fissura Perigosa | OK | Pendente | Em andamento |
| 34 | Pandemia | OK | Pendente | Em andamento |
| 35 | Rede Social | OK | Pendente | Em andamento |
| 36 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 37 | Torre de dados | OK | Pendente | Em andamento |
| 38 | Trem da mina | OK | Pendente | Em andamento |
| 39 | Divisão do Tesouro | OK | Pendente | Em andamento |
| 40 | Três por Dois | OK | Pendente | Em andamento |
| 41 | Emoticons | OK | Pendente | Em andamento |
| 42 | Acelerador de partículas | OK | Pendente | Em andamento |
| 43 | Fissura Perigosa | OK | Pendente | Em andamento |
| 44 | Bingo! | OK | Pendente | Em andamento |
| 45 | Paciente Zero | OK | Pendente | Em andamento |
| 46 | Dona Lesma | OK | Pendente | Em andamento |
| 47 | Palavras Cruzadas | OK | Pendente | Em andamento |
| 48 | Jogo dos Pinos | OK | Pendente | Em andamento |
| 49 | Piloto Automático | OK | Pendente | Em andamento |
| 50 | Entrega de Caixas | OK | Pendente | Em andamento |
| 51 | Escher | OK | Pendente | Em andamento |
| 52 | Dona Formiga | OK | Pendente | Em andamento |
| 53 | Fotografia | OK | Pendente | Em andamento |
| 54 | Quebra-cabeças | OK | Pendente | Em andamento |
| 55 | Estrada | OK | Pendente | Em andamento |
| 56 | Atlanta | OK | Pendente | Em andamento |
| 57 | Candidatas | OK | Pendente | Em andamento |
| 58 | Rede social | OK | Pendente | Em andamento |
| 59 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 60 | Trem da mina | OK | Pendente | Em andamento |


### OBI 2019

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Dominó | OK | Pendente | Em andamento |
| 2 | A idade de Dona Mônica | OK | Pendente | Em andamento |
| 3 | Sequência Secreta | OK | Pendente | Em andamento |
| 4 | Metrô da Nlogônia | OK | Pendente | Em andamento |
| 5 | Mesa redonda | OK | Pendente | Em andamento |
| 6 | Exploração do Capitão Levi | OK | Pendente | Em andamento |
| 7 | Grand Prix da Nlogônia | OK | Pendente | Em andamento |
| 8 | Etiquetas | OK | Pendente | Em andamento |
| 9 | Nota esquecida | OK | Pendente | Em andamento |
| 10 | Tabela do campeonato | OK | Pendente | Em andamento |
| 11 | Jogo dos copos | OK | Pendente | Em andamento |
| 12 | Xadrez Aleatório | OK | Pendente | Em andamento |
| 13 | Metrô da Nlogônia | OK | Pendente | Em andamento |
| 14 | Mesa redonda | OK | Pendente | Em andamento |
| 15 | Computador | OK | Pendente | Em andamento |
| 16 | Etiquetas | OK | Pendente | Em andamento |
| 17 | Detetive | OK | Pendente | Em andamento |
| 18 | Matriz super-legal | OK | Pendente | Em andamento |
| 19 | Supermercado | OK | Pendente | Em andamento |
| 20 | Calçada Imperial | OK | Pendente | Em andamento |
| 21 | A idade de Dona Mônica | OK | Pendente | Em andamento |
| 22 | Soma | OK | Pendente | Em andamento |
| 23 | Chuva | OK | Pendente | Em andamento |
| 24 | Coleção de Upas | OK | Pendente | Em andamento |
| 25 | Linhas de Ônibus | OK | Pendente | Em andamento |
| 26 | Parcelamento sem juros | OK | Pendente | Em andamento |
| 27 | Manchas de pele | OK | Pendente | Em andamento |
| 28 | Matriz super-legal | OK | Pendente | Em andamento |
| 29 | Nota esquecida | OK | Pendente | Em andamento |
| 30 | Ponto do meio | OK | Pendente | Em andamento |
| 31 | Pares de números | OK | Pendente | Em andamento |
| 32 | Parcelamento sem juros | OK | Pendente | Em andamento |
| 33 | Manchas de pele | OK | Pendente | Em andamento |
| 34 | Nota cortada | OK | Pendente | Em andamento |
| 35 | A idade de Dona Mônica | OK | Pendente | Em andamento |
| 36 | Jogo de Dominós | OK | Pendente | Em andamento |
| 37 | Distância entre amigos | OK | Pendente | Em andamento |


### OBI 2018

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Piso da escola | OK | Pendente | Em andamento |
| 2 | Figurinhas da copa | OK | Pendente | Em andamento |
| 3 | Câmara de Compensação | OK | Pendente | Em andamento |
| 4 | Fuga | OK | Pendente | Em andamento |
| 5 | Elevador | OK | Pendente | Em andamento |
| 6 | Wifi | OK | Pendente | Em andamento |
| 7 | Cinco | OK | Pendente | Em andamento |
| 8 | Muro | OK | Pendente | Em andamento |
| 9 | Baldes | OK | Pendente | Em andamento |
| 10 | Maximin | OK | Pendente | Em andamento |
| 11 | Bolas | OK | Pendente | Em andamento |
| 12 | Piso da escola | OK | Pendente | Em andamento |
| 13 | Figurinhas da Copa | OK | Pendente | Em andamento |
| 14 | Ilhas | OK | Pendente | Em andamento |
| 15 | Xadrez | OK | Pendente | Em andamento |
| 16 | Escadinha | OK | Pendente | Em andamento |
| 17 | Pirâmide | OK | Pendente | Em andamento |
| 18 | Cinco | OK | Pendente | Em andamento |
| 19 | Muro | OK | Pendente | Em andamento |
| 20 | Baldes | OK | Pendente | Em andamento |
| 21 | Mancha | OK | Pendente | Em andamento |
| 22 | Bolas | OK | Pendente | Em andamento |
| 23 | Fuga | OK | Pendente | Em andamento |
| 24 | Elevador | OK | Pendente | Em andamento |
| 25 | Sequência | OK | Pendente | Em andamento |
| 26 | Batalha | OK | Pendente | Em andamento |
| 27 | Troca | OK | Pendente | Em andamento |
| 28 | Pulo do Gato | OK | Pendente | Em andamento |
| 29 | Copa | OK | Pendente | Em andamento |
| 30 | Pesos | OK | Pendente | Em andamento |
| 31 | Cápsulas | OK | Pendente | Em andamento |
| 32 | Campeonato | OK | Pendente | Em andamento |
| 33 | Cápsulas | OK | Pendente | Em andamento |
| 34 | Relógios | OK | Pendente | Em andamento |
| 35 | Batalha | OK | Pendente | Em andamento |
| 36 | Troca | OK | Pendente | Em andamento |
| 37 | Recibo de Compra | OK | Pendente | Em andamento |
| 38 | Pulo do Gato | OK | Pendente | Em andamento |
| 39 | Basquete de robôs | OK | Pendente | Em andamento |
| 40 | Álbum da copa | OK | Pendente | Em andamento |


### OBI 2017

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Zip | OK | Pendente | Em andamento |
| 2 | Gomoku | OK | Pendente | Em andamento |
| 3 | Visita entre cidades | OK | Pendente | Em andamento |
| 4 | Bits | OK | Pendente | Em andamento |
| 5 | Game-10 | OK | Pendente | Em andamento |
| 6 | Palíndromo | OK | Pendente | Em andamento |
| 7 | Botas Trocadas | OK | Pendente | Em andamento |
| 8 | Teleférico | OK | Pendente | Em andamento |
| 9 | Segredo do Cofre | OK | Pendente | Em andamento |
| 10 | Zip | OK | Pendente | Em andamento |
| 11 | Ônibus | OK | Pendente | Em andamento |
| 12 | Gomoku | OK | Pendente | Em andamento |
| 13 | Game-10 | OK | Pendente | Em andamento |
| 14 | Chefe | OK | Pendente | Em andamento |
| 15 | Botas Trocadas | OK | Pendente | Em andamento |
| 16 | Dario e Xerxes | OK | Pendente | Em andamento |
| 17 | Mapa | OK | Pendente | Em andamento |
| 18 | Cortando o Papel | OK | Pendente | Em andamento |
| 19 | Frete | OK | Pendente | Em andamento |
| 20 | Bondinho | OK | Pendente | Em andamento |
| 21 | Drone de Entrega | OK | Pendente | Em andamento |
| 22 | Taxa | OK | Pendente | Em andamento |
| 23 | Postes | OK | Pendente | Em andamento |
| 24 | Dividindo o império | OK | Pendente | Em andamento |
| 25 | Arranha-céu | OK | Pendente | Em andamento |
| 26 | Código | OK | Pendente | Em andamento |
| 27 | Carrinho | OK | Pendente | Em andamento |
| 28 | Postes | OK | Pendente | Em andamento |
| 29 | Dividindo o império | OK | Pendente | Em andamento |
| 30 | Arranha-céu | OK | Pendente | Em andamento |
| 31 | Código | OK | Pendente | Em andamento |
| 32 | Montanha | OK | Pendente | Em andamento |
| 33 | Jogo de Tabuleiro | OK | Pendente | Em andamento |
| 34 | Castelos da Nlogônia | OK | Pendente | Em andamento |
| 35 | Dario e Xerxes | OK | Pendente | Em andamento |
| 36 | Mapa | OK | Pendente | Em andamento |
| 37 | Cortando o Papel | OK | Pendente | Em andamento |
| 38 | Frete | OK | Pendente | Em andamento |
| 39 | Cartas | OK | Pendente | Em andamento |
| 40 | Montanha | OK | Pendente | Em andamento |
| 41 | Jogo de Tabuleiro | OK | Pendente | Em andamento |


### OBI 2016

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Pô, que mão | OK | Pendente | Em andamento |
| 2 | Jardim de infância | OK | Pendente | Em andamento |
| 3 | Quase primo | OK | Pendente | Em andamento |
| 4 | Falta uma | OK | Pendente | Em andamento |
| 5 | Ciclovias | OK | Pendente | Em andamento |
| 6 | Lâmpadas do hotel | OK | Pendente | Em andamento |
| 7 | Chaves | OK | Pendente | Em andamento |
| 8 | Chuva | OK | Pendente | Em andamento |
| 9 | Toca do Saci | OK | Pendente | Em andamento |
| 10 | Sanduíche | OK | Pendente | Em andamento |
| 11 | Medalhas | OK | Pendente | Em andamento |
| 12 | Caverna de Ordinskaya | OK | Pendente | Em andamento |
| 13 | Arco e flecha | OK | Pendente | Em andamento |
| 14 | Caminhos do reino | OK | Pendente | Em andamento |
| 15 | Lâmpadas do hotel | OK | Pendente | Em andamento |
| 16 | Chaves | OK | Pendente | Em andamento |
| 17 | Chuva | OK | Pendente | Em andamento |
| 18 | Nova avenida | OK | Pendente | Em andamento |
| 19 | Direção | OK | Pendente | Em andamento |
| 20 | Pô, que mão | OK | Pendente | Em andamento |
| 21 | Times | OK | Pendente | Em andamento |
| 22 | Jardim de infância | OK | Pendente | Em andamento |
| 23 | Arco e flecha | OK | Pendente | Em andamento |
| 24 | Ciclovias | OK | Pendente | Em andamento |
| 25 | Jogo de par ou ímpar | OK | Pendente | Em andamento |
| 26 | Lâmpadas | OK | Pendente | Em andamento |
| 27 | Tacos de bilhar | OK | Pendente | Em andamento |
| 28 | Clube dos Cinco | OK | Pendente | Em andamento |
| 29 | Plantação de morango | OK | Pendente | Em andamento |
| 30 | Jogo de par ou ímpar | OK | Pendente | Em andamento |
| 31 | Lâmpadas | OK | Pendente | Em andamento |
| 32 | Medalhas | OK | Pendente | Em andamento |
| 33 | Gincana | OK | Pendente | Em andamento |
| 34 | Caverna de Ordinskaya | OK | Pendente | Em andamento |
| 35 | Fuga com helicóptero | OK | Pendente | Em andamento |


### OBI 2015

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Móbile | OK | Pendente | Em andamento |
| 2 | Linhas Cruzadas | OK | Pendente | Em andamento |
| 3 | Fita Colorida | OK | Pendente | Em andamento |
| 4 | Arquivos | OK | Pendente | Em andamento |
| 5 | Impedido! | OK | Pendente | Em andamento |
| 6 | Torre | OK | Pendente | Em andamento |
| 7 | Código | OK | Pendente | Em andamento |
| 8 | Cobra coral | OK | Pendente | Em andamento |
| 9 | Quebra-cabeça | OK | Pendente | Em andamento |
| 10 | Família real | OK | Pendente | Em andamento |
| 11 | Caixinha de palitos | OK | Pendente | Em andamento |
| 12 | Banco Inteligente | OK | Pendente | Em andamento |
| 13 | Móbile | OK | Pendente | Em andamento |
| 14 | Fita Colorida | OK | Pendente | Em andamento |
| 15 | Prêmio do Milhão | OK | Pendente | Em andamento |
| 16 | Macacos me mordam! | OK | Pendente | Em andamento |
| 17 | Chocolate em barra | OK | Pendente | Em andamento |
| 18 | Mina | OK | Pendente | Em andamento |
| 19 | Cálculo | OK | Pendente | Em andamento |
| 20 | Fila | OK | Pendente | Em andamento |
| 21 | Impedimento! | OK | Pendente | Em andamento |
| 22 | Capitais | OK | Pendente | Em andamento |
| 23 | Letras | OK | Pendente | Em andamento |
| 24 | Torre | OK | Pendente | Em andamento |


### OBI 2014

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Flíper | OK | Pendente | Em andamento |
| 2 | Gangorra | OK | Pendente | Em andamento |
| 3 | Fila | OK | Pendente | Em andamento |
| 4 | Notas | OK | Pendente | Em andamento |
| 5 | Tapetes | OK | Pendente | Em andamento |
| 6 | Blefe | OK | Pendente | Em andamento |
| 7 | Mapa | OK | Pendente | Em andamento |
| 8 | Frequência | OK | Pendente | Em andamento |
| 9 | Copa do Mundo | OK | Pendente | Em andamento |
| 10 | Língua do P | OK | Pendente | Em andamento |
| 11 | PacMan | OK | Pendente | Em andamento |
| 12 | Fechadura | OK | Pendente | Em andamento |
| 13 | Matriz Escada | OK | Pendente | Em andamento |
| 14 | Loteria | OK | Pendente | Em andamento |
| 15 | Sinuca | OK | Pendente | Em andamento |
| 16 | Passa Bolinha | OK | Pendente | Em andamento |
| 17 | Decifra | OK | Pendente | Em andamento |
| 18 | Quadrado | OK | Pendente | Em andamento |
| 19 | Corredor | OK | Pendente | Em andamento |
| 20 | Jogo da Memória | OK | Pendente | Em andamento |
| 21 | Triângulo | OK | Pendente | Em andamento |
| 22 | Setas | OK | Pendente | Em andamento |
| 23 | Semente | OK | Pendente | Em andamento |
| 24 | Letras | OK | Pendente | Em andamento |


### OBI 2013

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Lençol | OK | Pendente | Em andamento |
| 2 | Tiro ao Alvo | OK | Pendente | Em andamento |
| 3 | Catálogo de Músicas | OK | Pendente | Em andamento |
| 4 | Vende-se | OK | Pendente | Em andamento |
| 5 | Saldo do Vovô | OK | Pendente | Em andamento |
| 6 | Tomadas | OK | Pendente | Em andamento |
| 7 | Capital | OK | Pendente | Em andamento |
| 8 | Corrida | OK | Pendente | Em andamento |
| 9 | Capital | OK | Pendente | Em andamento |
| 10 | Rodovia | OK | Pendente | Em andamento |
| 11 | Robô | OK | Pendente | Em andamento |


### OBI 2012

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Carnaval | OK | Pendente | Em andamento |
| 2 | Costa | OK | Pendente | Em andamento |
| 3 | Guerra por território | OK | Pendente | Em andamento |
| 4 | Chocolate | OK | Pendente | Em andamento |
| 5 | Tira-teima | OK | Pendente | Em andamento |
| 6 | Receita de Bolo | OK | Pendente | Em andamento |
| 7 | Álbum de fotos | OK | Pendente | Em andamento |
| 8 | Soma das casas | OK | Pendente | Em andamento |
| 9 | Bomba | OK | Pendente | Em andamento |
| 10 | Banco | OK | Pendente | Em andamento |
| 11 | Campeonato | OK | Pendente | Em andamento |
| 12 | Busca na Internet | OK | Pendente | Em andamento |
| 13 | Desafio do maior número | OK | Pendente | Em andamento |
| 14 | Vice-campeão | OK | Pendente | Em andamento |
| 15 | Corrida | OK | Pendente | Em andamento |
| 16 | Consecutivos | OK | Pendente | Em andamento |
| 17 | Colchão | OK | Pendente | Em andamento |
| 18 | Tabuleiro Esburacado | OK | Pendente | Em andamento |
| 19 | Frequencia na aula | OK | Pendente | Em andamento |
| 20 | Tarzan | OK | Pendente | Em andamento |


### OBI 2011

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Calculadora | OK | Pendente | Em andamento |
| 2 | Colorindo | OK | Pendente | Em andamento |
| 3 | Balé | OK | Pendente | Em andamento |
| 4 | Selos | OK | Pendente | Em andamento |
| 5 | Chuva | OK | Pendente | Em andamento |
| 6 | Gincana | OK | Pendente | Em andamento |
| 7 | Calculadora | OK | Pendente | Em andamento |
| 8 | Corrida | OK | Pendente | Em andamento |
| 9 | Progressões Aritméticas | OK | Pendente | Em andamento |
| 10 | Pulo do Sapo | OK | Pendente | Em andamento |
| 11 | Triângulos | OK | Pendente | Em andamento |
| 12 | Quadrado Mágico | OK | Pendente | Em andamento |
| 13 | Expressões | OK | Pendente | Em andamento |
| 14 | Escalonamento ótimo | OK | Pendente | Em andamento |
| 15 | Reduzindo detalhes em um mapa | OK | Pendente | Em andamento |
| 16 | Vira! | OK | Pendente | Em andamento |
| 17 | O mar não está para peixe | OK | Pendente | Em andamento |
| 18 | Caça ao Tesouro | OK | Pendente | Em andamento |
| 19 | Desafio cartográfico | OK | Pendente | Em andamento |
| 20 | Quadrado Aritmético | OK | Pendente | Em andamento |
| 21 | Transporte de Contêineres | OK | Pendente | Em andamento |
| 22 | Campo Minado | OK | Pendente | Em andamento |
| 23 | Corrida | OK | Pendente | Em andamento |


### OBI 2010

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Floresta | OK | Pendente | Em andamento |
| 2 | Altas Aventuras | OK | Pendente | Em andamento |
| 3 | Tradutor alienígena | OK | Pendente | Em andamento |
| 4 | Multiplicação de matrizes | OK | Pendente | Em andamento |
| 5 | Telescópio | OK | Pendente | Em andamento |
| 6 | Pneu | OK | Pendente | Em andamento |
| 7 | Garçom | OK | Pendente | Em andamento |
| 8 | SEDEX | OK | Pendente | Em andamento |
| 9 | Cometa | OK | Pendente | Em andamento |
| 10 | Batalha Naval | OK | Pendente | Em andamento |
| 11 | Elevador | OK | Pendente | Em andamento |
| 12 | Reunião | OK | Pendente | Em andamento |
| 13 | Escada Rolante | OK | Pendente | Em andamento |
| 14 | Tacógrafo | OK | Pendente | Em andamento |
| 15 | Dentista | OK | Pendente | Em andamento |
| 16 | Sedex Marciano | OK | Pendente | Em andamento |
| 17 | Fusões | OK | Pendente | Em andamento |
| 18 | Lista de Chamada | OK | Pendente | Em andamento |
| 19 | Dança Indígena | OK | Pendente | Em andamento |
| 20 | Conta de água | OK | Pendente | Em andamento |
| 21 | Pedágio | OK | Pendente | Em andamento |
| 22 | Times | OK | Pendente | Em andamento |
| 23 | Copa do Mundo | OK | Pendente | Em andamento |


### OBI 2009

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Aviões de papel | OK | Pendente | Em andamento |
| 2 | Overflow | OK | Pendente | Em andamento |
| 3 | Número de Envelopes | OK | Pendente | Em andamento |
| 4 | Feira de Bactérias | OK | Pendente | Em andamento |
| 5 | Notas da Prova | OK | Pendente | Em andamento |
| 6 | Caçadores de Mitos | OK | Pendente | Em andamento |
| 7 | Caminho das Pontes | OK | Pendente | Em andamento |
| 8 | O Fugitivo | OK | Pendente | Em andamento |
| 9 | Maratona | OK | Pendente | Em andamento |
| 10 | Competição de chocolate | OK | Pendente | Em andamento |
| 11 | Olimpíadas | OK | Pendente | Em andamento |
| 12 | Banda | OK | Pendente | Em andamento |
| 13 | Aviões de papel | OK | Pendente | Em andamento |
| 14 | Número de Envelopes | OK | Pendente | Em andamento |
| 15 | Overflow | OK | Pendente | Em andamento |
| 16 | Maratona | OK | Pendente | Em andamento |
| 17 | Competição de chocolate | OK | Pendente | Em andamento |
| 18 | Olimpíadas | OK | Pendente | Em andamento |
| 19 | Banda | OK | Pendente | Em andamento |
| 20 | Olimpíadas | OK | Pendente | Em andamento |
| 21 | Simulador | OK | Pendente | Em andamento |
| 22 | Cadeiras do auditório | OK | Pendente | Em andamento |
| 23 | Banda | OK | Pendente | Em andamento |
| 24 | Competição de chocolate | OK | Pendente | Em andamento |


### OBI 2008

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | OBI | OK | Pendente | Em andamento |
| 2 | Telefone | OK | Pendente | Em andamento |
| 3 | Avião | OK | Pendente | Em andamento |
| 4 | Lanche na empresa | OK | Pendente | Em andamento |
| 5 | Ogros | OK | Pendente | Em andamento |
| 6 | Auto Estrada | OK | Pendente | Em andamento |
| 7 | Chuva | OK | Pendente | Em andamento |
| 8 | Ortografia | OK | Pendente | Em andamento |
| 9 | Frete da Família Silva | OK | Pendente | Em andamento |
| 10 | OBI | OK | Pendente | Em andamento |
| 11 | Insensibilidade | OK | Pendente | Em andamento |
| 12 | Telefone | OK | Pendente | Em andamento |
| 13 | Auto Estrada | OK | Pendente | Em andamento |
| 14 | Viagem Espacial | OK | Pendente | Em andamento |
| 15 | Cavalos | OK | Pendente | Em andamento |
| 16 | Auto Estrada | OK | Pendente | Em andamento |
| 17 | Mini Calculadora | OK | Pendente | Em andamento |
| 18 | Ações da Bolsa | OK | Pendente | Em andamento |
| 19 | OBI | OK | Pendente | Em andamento |
| 20 | Telefone | OK | Pendente | Em andamento |
| 21 | Vestibular | OK | Pendente | Em andamento |


### OBI 2007

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Chocolate | OK | Pendente | Em andamento |
| 2 | Repositórios | OK | Pendente | Em andamento |
| 3 | Sacoleiro | OK | Pendente | Em andamento |
| 4 | Pastas | OK | Pendente | Em andamento |
| 5 | Móbile | OK | Pendente | Em andamento |
| 6 | Telemarketing | OK | Pendente | Em andamento |
| 7 | Pão a Metro | OK | Pendente | Em andamento |
| 8 | Uiquipédia | OK | Pendente | Em andamento |
| 9 | Detectando Colisões | OK | Pendente | Em andamento |
| 10 | Peça Perdida | OK | Pendente | Em andamento |
| 11 | Quadrado Mágico | OK | Pendente | Em andamento |
| 12 | Telemarketing | OK | Pendente | Em andamento |
| 13 | Pizza | OK | Pendente | Em andamento |
| 14 | Labirinto | OK | Pendente | Em andamento |


### OBI 2006

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Penalidade mínima | OK | Pendente | Em andamento |
| 2 | Lobo Mau | OK | Pendente | Em andamento |
| 3 | Sub-seqüências | OK | Pendente | Em andamento |
| 4 | Lobo Mau | OK | Pendente | Em andamento |
| 5 | Autorama | OK | Pendente | Em andamento |
| 6 | Quadrado Mágico | OK | Pendente | Em andamento |
| 7 | Monopólio | OK | Pendente | Em andamento |
| 8 | Margaridas | OK | Pendente | Em andamento |
| 9 | Conversa não tão secreta | OK | Pendente | Em andamento |
| 10 | Truco | OK | Pendente | Em andamento |
| 11 | Colheita de Caju | OK | Pendente | Em andamento |
| 12 | Museu | OK | Pendente | Em andamento |
| 13 | Jogo de Cartas | OK | Pendente | Em andamento |
| 14 | Escada perfeita | OK | Pendente | Em andamento |


### OBI 2005

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Frota de Táxi | OK | Pendente | Em andamento |
| 2 | Campo de Minhocas | OK | Pendente | Em andamento |
| 3 | Duende Perdido | OK | Pendente | Em andamento |
| 4 | Trilhas | OK | Pendente | Em andamento |
| 5 | Bafo | OK | Pendente | Em andamento |
| 6 | Transmissão de Energia | OK | Pendente | Em andamento |
| 7 | Vivo ou Morto | OK | Pendente | Em andamento |
| 8 | Pedido de Desculpas | OK | Pendente | Em andamento |
| 9 | Mini-Poker | OK | Pendente | Em andamento |


### OBI 2004

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Par ou ímpar | OK | Pendente | Em andamento |
| 2 | Cubra os Furos | OK | Pendente | Em andamento |
| 3 | Palíndrome | OK | Pendente | Em andamento |
| 4 | TV da Vovó | OK | Pendente | Em andamento |
| 5 | Proteja sua senha | OK | Pendente | Em andamento |
| 6 | Orkut | OK | Pendente | Em andamento |


### OBI 2003

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Cofrinhos da Vó Vitória | OK | Pendente | Em andamento |
| 2 | Estágio | OK | Pendente | Em andamento |
| 3 | Torres de Hanói | OK | Pendente | Em andamento |
| 4 | Supermercado | OK | Pendente | Em andamento |
| 5 | Número de Erdos | OK | Pendente | Em andamento |
| 6 | Tetris | OK | Pendente | Em andamento |


### OBI 2002

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Temperatura Lunar | OK | Pendente | Em andamento |
| 2 | Caça ao Tesouro | OK | Pendente | Em andamento |
| 3 | Dobradura | OK | Pendente | Em andamento |
| 4 | Aeroporto | OK | Pendente | Em andamento |
| 5 | Pedágio | OK | Pendente | Em andamento |


### OBI 2001

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Meteoros | OK | Pendente | Em andamento |
| 2 | Dominó | OK | Pendente | Em andamento |
| 3 | Dengue | OK | Pendente | Em andamento |
| 4 | Sorvete | OK | Pendente | Em andamento |
| 5 | Calculando | OK | Pendente | Em andamento |


### OBI 2000

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Rede ótica | OK | Pendente | Em andamento |
| 2 | Quermesse | OK | Pendente | Em andamento |
| 3 | Bits Trocados | OK | Pendente | Em andamento |
| 4 | Saldo de gols | OK | Pendente | Em andamento |
| 5 | Macaco-prego | OK | Pendente | Em andamento |

