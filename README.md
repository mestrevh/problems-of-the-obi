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
| 26 | Avenida | OK | Pendente | Em andamento |
| 27 | Alfabeto alienígena | OK | Pendente | Em andamento |
| 28 | Atletismo | OK | Pendente | Em andamento |
| 29 | Brigadeiros | OK | Pendente | Em andamento |
| 30 | Construtora | OK | Pendente | Em andamento |
| 31 | Retas | OK | Pendente | Em andamento |
| 32 | Burocracia | OK | Pendente | Em andamento |
| 33 | Jogo de Pratos | OK | Pendente | Em andamento |


### OBI 2023

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Pizza da OBI | OK | Pendente | Em andamento |
| 2 | Código de Compressão | OK | Pendente | Em andamento |
| 3 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 4 | Ogro | OK | Pendente | Em andamento |
| 5 | Relógio | OK | Pendente | Em andamento |
| 6 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 7 | Jogo da Vida | OK | Pendente | Em andamento |
| 8 | Código de compressão | OK | Pendente | Em andamento |
| 9 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 10 | Intervalo Distinto | OK | Pendente | Em andamento |
| 11 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 12 | Prefixo | OK | Pendente | Em andamento |
| 13 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 14 | Intervalo Distinto | OK | Pendente | Em andamento |
| 15 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 16 | Pirâmide | OK | Pendente | Em andamento |
| 17 | Transportes | OK | Pendente | Em andamento |
| 18 | Oficina Mecânica | OK | Pendente | Em andamento |
| 19 | Trio de Bonecas | OK | Pendente | Em andamento |
| 20 | Fast-Food | OK | Pendente | Em andamento |
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
| 39 | Ogro | OK | Pendente | Em andamento |
| 40 | Concurso | ❌ | Inviável | ❌ Sem casos de teste |
| 41 | Bactérias | OK | Pendente | Em andamento |
| 42 | Contas a pagar | OK | Pendente | Em andamento |
| 43 | Leilão | OK | Pendente | Em andamento |
| 44 | Estoque | OK | Pendente | Em andamento |
| 45 | Toupeira | OK | Pendente | Em andamento |
| 46 | Contas a pagar | OK | Pendente | Em andamento |
| 47 | Estoque | OK | Pendente | Em andamento |
| 48 | Subsequência | OK | Pendente | Em andamento |
| 49 | Sr. Toupeira | OK | Pendente | Em andamento |
| 50 | Prefixo | OK | Pendente | Em andamento |
| 51 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 52 | Intervalo Distinto | OK | Pendente | Em andamento |
| 53 | Barcos da Nlogônia | OK | Pendente | Em andamento |
| 54 | Cabo de guerra | OK | Pendente | Em andamento |
| 55 | Tesouro | OK | Pendente | Em andamento |
| 56 | Metrônibus | OK | Pendente | Em andamento |
| 57 | Oficina Mecânica | OK | Pendente | Em andamento |
| 58 | Prefixo | OK | Pendente | Em andamento |
| 59 | Grupos de Trabalho | OK | Pendente | Em andamento |
| 60 | Intervalo Distinto | OK | Pendente | Em andamento |
| 61 | Pirâmide | OK | Pendente | Em andamento |
| 62 | Transportes | OK | Pendente | Em andamento |
| 63 | Oficina Mecânica | OK | Pendente | Em andamento |
| 64 | Trio de Bonecas | OK | Pendente | Em andamento |
| 65 | Fast-Food | OK | Pendente | Em andamento |


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
| 13 | Hotel | OK | Pendente | Em andamento |
| 14 | Maior valor | OK | Pendente | Em andamento |
| 15 | Quadrado Mágico | OK | Pendente | Em andamento |
| 16 | Chuva | OK | Pendente | Em andamento |
| 17 | Cinema | OK | Pendente | Em andamento |
| 18 | Hotel | OK | Pendente | Em andamento |
| 19 | Show | OK | Pendente | Em andamento |
| 20 | Tanque de combustível | OK | Pendente | Em andamento |
| 21 | Pirâmide | OK | Pendente | Em andamento |
| 22 | Câmeras | OK | Pendente | Em andamento |
| 23 | Tanque de combustível | OK | Pendente | Em andamento |
| 24 | Pirâmide | OK | Pendente | Em andamento |
| 25 | Subcadeias | OK | Pendente | Em andamento |
| 26 | Viagem | OK | Pendente | Em andamento |
| 27 | Troféu | OK | Pendente | Em andamento |
| 28 | Câmeras | OK | Pendente | Em andamento |
| 29 | Subcadeias | OK | Pendente | Em andamento |
| 30 | Viagem | OK | Pendente | Em andamento |
| 31 | Jogo | OK | Pendente | Em andamento |
| 32 | Teste de redação | OK | Pendente | Em andamento |
| 33 | Carro elétrico | OK | Pendente | Em andamento |
| 34 | Dígitos | OK | Pendente | Em andamento |


### OBI 2021

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Dupla de tênis | OK | Pendente | Em andamento |
| 2 | Passatempo | OK | Pendente | Em andamento |
| 3 | Sanduíche | OK | Pendente | Em andamento |
| 4 | Retângulo | OK | Pendente | Em andamento |
| 5 | Idade de Camila | OK | Pendente | Em andamento |
| 6 | Plano de Internet | OK | Pendente | Em andamento |
| 7 | Torneio de tênis | OK | Pendente | Em andamento |
| 8 | Torneio de tênis | OK | Pendente | Em andamento |
| 9 | Tempo de resposta | OK | Pendente | Em andamento |
| 10 | Zero para cancelar | OK | Pendente | Em andamento |
| 11 | Ogro | OK | Pendente | Em andamento |
| 12 | Casamento de inteiros | OK | Pendente | Em andamento |
| 13 | Sr. Sapo | OK | Pendente | Em andamento |
| 14 | Plano de estacionamento | OK | Pendente | Em andamento |
| 15 | Duplas de tênis | OK | Pendente | Em andamento |
| 16 | Pangrama | OK | Pendente | Em andamento |
| 17 | Robô | OK | Pendente | Em andamento |
| 18 | Média e mediana | OK | Pendente | Em andamento |
| 19 | Recorde | OK | Pendente | Em andamento |
| 20 | Potência | OK | Pendente | Em andamento |
| 21 | Cálculo rápido | OK | Pendente | Em andamento |
| 22 | Lista palíndroma | OK | Pendente | Em andamento |
| 23 | Duplas de tênis | OK | Pendente | Em andamento |
| 24 | Retângulo | OK | Pendente | Em andamento |
| 25 | Robô | OK | Pendente | Em andamento |
| 26 | Média e mediana | OK | Pendente | Em andamento |
| 27 | Cálculo rápido | OK | Pendente | Em andamento |
| 28 | Lista palíndroma | OK | Pendente | Em andamento |
| 29 | Poligrama | OK | Pendente | Em andamento |
| 30 | Senha da Vó Zinha | OK | Pendente | Em andamento |
| 31 | Idade de Camila | OK | Pendente | Em andamento |
| 32 | Zero para cancelar | OK | Pendente | Em andamento |
| 33 | Tempo de resposta | OK | Pendente | Em andamento |
| 34 | Cifra da Nlogônia | OK | Pendente | Em andamento |
| 35 | Mínimo e máximo | OK | Pendente | Em andamento |
| 36 | Lista palíndroma | OK | Pendente | Em andamento |
| 37 | Poligrama | OK | Pendente | Em andamento |
| 38 | Senha da Vó Zinha | OK | Pendente | Em andamento |
| 39 | Ogro | OK | Pendente | Em andamento |
| 40 | Teclado | OK | Pendente | Em andamento |
| 41 | Falha de segurança | OK | Pendente | Em andamento |
| 42 | Festa olímpica | OK | Pendente | Em andamento |
| 43 | Dona Minhoca | OK | Pendente | Em andamento |
| 44 | Casamento de inteiros | OK | Pendente | Em andamento |
| 45 | Sr. Sapo | OK | Pendente | Em andamento |
| 46 | Festa olímpica | OK | Pendente | Em andamento |
| 47 | Plano de estacionamento | OK | Pendente | Em andamento |
| 48 | Recorde | OK | Pendente | Em andamento |
| 49 | Anagrama | OK | Pendente | Em andamento |
| 50 | Potência | OK | Pendente | Em andamento |
| 51 | Pesquisa de preços | OK | Pendente | Em andamento |
| 52 | Casamento de inteiros | OK | Pendente | Em andamento |
| 53 | Cubo e quadrado | OK | Pendente | Em andamento |
| 54 | Festa olímpica | OK | Pendente | Em andamento |
| 55 | Falha de segurança | OK | Pendente | Em andamento |
| 56 | Dona Minhoca | OK | Pendente | Em andamento |


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
| 12 | Torre de dados | OK | Pendente | Em andamento |
| 13 | Candidatas | OK | Pendente | Em andamento |
| 14 | Aplicativo de calorias | OK | Pendente | Em andamento |
| 15 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 16 | Trem da mina | OK | Pendente | Em andamento |
| 17 | Dona Formiga | OK | Pendente | Em andamento |
| 18 | Fotografia | OK | Pendente | Em andamento |
| 19 | Quebra-cabeças | OK | Pendente | Em andamento |
| 20 | Estrada | OK | Pendente | Em andamento |
| 21 | Dona Formiga | OK | Pendente | Em andamento |
| 22 | Fotografia | OK | Pendente | Em andamento |
| 23 | Caixeiro Viajante | OK | Pendente | Em andamento |
| 24 | Estrada | OK | Pendente | Em andamento |
| 25 | Irmãos | OK | Pendente | Em andamento |
| 26 | Garamana | OK | Pendente | Em andamento |
| 27 | Camisetas da Olimpíada | OK | Pendente | Em andamento |
| 28 | Música para Todos | OK | Pendente | Em andamento |
| 29 | Rede Social | OK | Pendente | Em andamento |
| 30 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 31 | Torre de dados | OK | Pendente | Em andamento |
| 32 | Trem da mina | OK | Pendente | Em andamento |
| 33 | Divisão do Tesouro | OK | Pendente | Em andamento |
| 34 | Três por Dois | OK | Pendente | Em andamento |
| 35 | Emoticons | OK | Pendente | Em andamento |
| 36 | Acelerador de partículas | OK | Pendente | Em andamento |
| 37 | Fissura Perigosa | OK | Pendente | Em andamento |
| 38 | Bingo! | OK | Pendente | Em andamento |
| 39 | Paciente Zero | OK | Pendente | Em andamento |
| 40 | Atlanta | OK | Pendente | Em andamento |
| 41 | Candidatas | OK | Pendente | Em andamento |
| 42 | Rede social | OK | Pendente | Em andamento |
| 43 | Jogo do Preto e Branco | OK | Pendente | Em andamento |
| 44 | Trem da mina | OK | Pendente | Em andamento |
| 45 | Dona Lesma | OK | Pendente | Em andamento |
| 46 | Palavras Cruzadas | OK | Pendente | Em andamento |
| 47 | Jogo dos Pinos | OK | Pendente | Em andamento |


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
| 12 | Nota cortada | OK | Pendente | Em andamento |
| 13 | A idade de Dona Mônica | OK | Pendente | Em andamento |
| 14 | Jogo de Dominós | OK | Pendente | Em andamento |
| 15 | Distância entre amigos | OK | Pendente | Em andamento |
| 16 | Detetive | OK | Pendente | Em andamento |
| 17 | Matriz super-legal | OK | Pendente | Em andamento |
| 18 | Supermercado | OK | Pendente | Em andamento |
| 19 | Matriz super-legal | OK | Pendente | Em andamento |
| 20 | Nota esquecida | OK | Pendente | Em andamento |
| 21 | Ponto do meio | OK | Pendente | Em andamento |
| 22 | Pares de números | OK | Pendente | Em andamento |
| 23 | Parcelamento sem juros | OK | Pendente | Em andamento |
| 24 | Manchas de pele | OK | Pendente | Em andamento |


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
| 18 | Fuga | OK | Pendente | Em andamento |
| 19 | Elevador | OK | Pendente | Em andamento |
| 20 | Sequência | OK | Pendente | Em andamento |
| 21 | Batalha | OK | Pendente | Em andamento |
| 22 | Troca | OK | Pendente | Em andamento |
| 23 | Pulo do Gato | OK | Pendente | Em andamento |
| 24 | Batalha | OK | Pendente | Em andamento |
| 25 | Troca | OK | Pendente | Em andamento |
| 26 | Recibo de Compra | OK | Pendente | Em andamento |
| 27 | Pulo do Gato | OK | Pendente | Em andamento |
| 28 | Basquete de robôs | OK | Pendente | Em andamento |
| 29 | Álbum da copa | OK | Pendente | Em andamento |


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
| 8 | Zip | OK | Pendente | Em andamento |
| 9 | Ônibus | OK | Pendente | Em andamento |
| 10 | Gomoku | OK | Pendente | Em andamento |
| 11 | Cartas | OK | Pendente | Em andamento |
| 12 | Montanha | OK | Pendente | Em andamento |
| 13 | Jogo de Tabuleiro | OK | Pendente | Em andamento |
| 14 | Game-10 | OK | Pendente | Em andamento |
| 15 | Chefe | OK | Pendente | Em andamento |
| 16 | Botas Trocadas | OK | Pendente | Em andamento |
| 17 | Dario e Xerxes | OK | Pendente | Em andamento |
| 18 | Mapa | OK | Pendente | Em andamento |
| 19 | Cortando o Papel | OK | Pendente | Em andamento |
| 20 | Frete | OK | Pendente | Em andamento |
| 21 | Bondinho | OK | Pendente | Em andamento |
| 22 | Drone de Entrega | OK | Pendente | Em andamento |
| 23 | Taxa | OK | Pendente | Em andamento |
| 24 | Postes | OK | Pendente | Em andamento |
| 25 | Dividindo o império | OK | Pendente | Em andamento |
| 26 | Arranha-céu | OK | Pendente | Em andamento |
| 27 | Código | OK | Pendente | Em andamento |
| 28 | Carrinho | OK | Pendente | Em andamento |
| 29 | Postes | OK | Pendente | Em andamento |
| 30 | Dividindo o império | OK | Pendente | Em andamento |
| 31 | Arranha-céu | OK | Pendente | Em andamento |
| 32 | Código | OK | Pendente | Em andamento |
| 33 | Montanha | OK | Pendente | Em andamento |
| 34 | Jogo de Tabuleiro | OK | Pendente | Em andamento |
| 35 | Castelos da Nlogônia | OK | Pendente | Em andamento |
| 36 | Dario e Xerxes | OK | Pendente | Em andamento |
| 37 | Mapa | OK | Pendente | Em andamento |
| 38 | Cortando o Papel | OK | Pendente | Em andamento |
| 39 | Frete | OK | Pendente | Em andamento |


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
| 12 | Gincana | OK | Pendente | Em andamento |
| 13 | Caverna de Ordinskaya | OK | Pendente | Em andamento |
| 14 | Fuga com helicóptero | OK | Pendente | Em andamento |
| 15 | Medalhas | OK | Pendente | Em andamento |
| 16 | Caverna de Ordinskaya | OK | Pendente | Em andamento |
| 17 | Arco e flecha | OK | Pendente | Em andamento |
| 18 | Caminhos do reino | OK | Pendente | Em andamento |
| 19 | Lâmpadas do hotel | OK | Pendente | Em andamento |
| 20 | Chaves | OK | Pendente | Em andamento |
| 21 | Chuva | OK | Pendente | Em andamento |
| 22 | Nova avenida | OK | Pendente | Em andamento |
| 23 | Direção | OK | Pendente | Em andamento |
| 24 | Jogo de par ou ímpar | OK | Pendente | Em andamento |
| 25 | Lâmpadas | OK | Pendente | Em andamento |
| 26 | Tacos de bilhar | OK | Pendente | Em andamento |
| 27 | Clube dos Cinco | OK | Pendente | Em andamento |
| 28 | Plantação de morango | OK | Pendente | Em andamento |
| 29 | Jogo de par ou ímpar | OK | Pendente | Em andamento |
| 30 | Lâmpadas | OK | Pendente | Em andamento |


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
| 16 | Impedimento! | OK | Pendente | Em andamento |
| 17 | Capitais | OK | Pendente | Em andamento |
| 18 | Letras | OK | Pendente | Em andamento |
| 19 | Torre | OK | Pendente | Em andamento |


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
| 9 | Decifra | OK | Pendente | Em andamento |
| 10 | Quadrado | OK | Pendente | Em andamento |
| 11 | Corredor | OK | Pendente | Em andamento |
| 12 | Jogo da Memória | OK | Pendente | Em andamento |


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
| 1 | Chocolate | OK | Pendente | Em andamento |
| 2 | Tira-teima | OK | Pendente | Em andamento |
| 3 | Receita de Bolo | OK | Pendente | Em andamento |
| 4 | Álbum de fotos | OK | Pendente | Em andamento |
| 5 | Soma das casas | OK | Pendente | Em andamento |
| 6 | Bomba | OK | Pendente | Em andamento |
| 7 | Banco | OK | Pendente | Em andamento |
| 8 | Vice-campeão | OK | Pendente | Em andamento |
| 9 | Corrida | OK | Pendente | Em andamento |
| 10 | Consecutivos | OK | Pendente | Em andamento |
| 11 | Colchão | OK | Pendente | Em andamento |
| 12 | O Tabuleiro Esburacado | OK | Pendente | Em andamento |
| 13 | Frequencia na aula | OK | Pendente | Em andamento |
| 14 | Tarzan | OK | Pendente | Em andamento |


### OBI 2011

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Transporte de Contêineres | OK | Pendente | Em andamento |
| 2 | Campo Minado | OK | Pendente | Em andamento |
| 3 | Corrida | OK | Pendente | Em andamento |
| 4 | Calculadora | OK | Pendente | Em andamento |
| 5 | Colorindo | OK | Pendente | Em andamento |
| 6 | Balé | OK | Pendente | Em andamento |
| 7 | Selos | OK | Pendente | Em andamento |
| 8 | Chuva | OK | Pendente | Em andamento |
| 9 | Gincana | OK | Pendente | Em andamento |
| 10 | Calculadora | OK | Pendente | Em andamento |
| 11 | Corrida | OK | Pendente | Em andamento |
| 12 | Progressões Aritméticas | OK | Pendente | Em andamento |
| 13 | Pulo do Sapo | OK | Pendente | Em andamento |
| 14 | Triângulos | OK | Pendente | Em andamento |
| 15 | Quadrado Mágico | OK | Pendente | Em andamento |
| 16 | Expressões | OK | Pendente | Em andamento |
| 17 | Escalonamento ótimo | OK | Pendente | Em andamento |
| 18 | Reduzindo detalhes em um mapa | OK | Pendente | Em andamento |
| 19 | Vira! | OK | Pendente | Em andamento |
| 20 | O mar não está para peixe | OK | Pendente | Em andamento |
| 21 | Caça ao Tesouro | OK | Pendente | Em andamento |
| 22 | Desafio cartográfico | OK | Pendente | Em andamento |
| 23 | Quadrado Aritmético | OK | Pendente | Em andamento |


### OBI 2010

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Sedex Marciano | OK | Pendente | Em andamento |
| 2 | Fusões | OK | Pendente | Em andamento |
| 3 | Lista de Chamada | OK | Pendente | Em andamento |
| 4 | Dança Indígena | OK | Pendente | Em andamento |
| 5 | Floresta | OK | Pendente | Em andamento |
| 6 | Altas Aventuras | OK | Pendente | Em andamento |
| 7 | Tradutor alienígena | OK | Pendente | Em andamento |
| 8 | Multiplicação de matrizes | OK | Pendente | Em andamento |
| 9 | Telescópio | OK | Pendente | Em andamento |
| 10 | Pneu | OK | Pendente | Em andamento |
| 11 | Garçom | OK | Pendente | Em andamento |
| 12 | SEDEX | OK | Pendente | Em andamento |
| 13 | Cometa | OK | Pendente | Em andamento |
| 14 | Batalha Naval | OK | Pendente | Em andamento |
| 15 | Elevador | OK | Pendente | Em andamento |
| 16 | Reunião | OK | Pendente | Em andamento |
| 17 | Escada Rolante | OK | Pendente | Em andamento |
| 18 | Tacógrafo | OK | Pendente | Em andamento |
| 19 | Dentista | OK | Pendente | Em andamento |


### OBI 2009

**Legenda de Status:**
* **Extração (API)**: `[OK]` significa que o script extraiu as informações com sucesso.
* **Testes (Manual)**: `[Pendente]` aguardando inserção humana, `[OK]` inserido.
* **Inviável**: Problema sem casos de teste ou fora do escopo.

| # | Problema | Extração (API) | Testes (Manual) | Status Final |
|:---:|:---|:---:|:---:|:---:|
| 1 | Olimpíadas | OK | Pendente | Em andamento |
| 2 | Simulador | OK | Pendente | Em andamento |
| 3 | Cadeiras do auditório | OK | Pendente | Em andamento |
| 4 | Banda | OK | Pendente | Em andamento |
| 5 | Competição de chocolate | OK | Pendente | Em andamento |
| 6 | Notas da Prova | OK | Pendente | Em andamento |
| 7 | Caçadores de Mitos | OK | Pendente | Em andamento |
| 8 | Caminho das Pontes | OK | Pendente | Em andamento |
| 9 | O Fugitivo | OK | Pendente | Em andamento |
| 10 | Maratona | OK | Pendente | Em andamento |
| 11 | Competição de chocolate | OK | Pendente | Em andamento |
| 12 | Olimpíadas | OK | Pendente | Em andamento |
| 13 | Banda | OK | Pendente | Em andamento |
| 14 | Aviões de papel | OK | Pendente | Em andamento |
| 15 | Número de Envelopes | OK | Pendente | Em andamento |
| 16 | Overflow | OK | Pendente | Em andamento |


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
| 6 | OBI | OK | Pendente | Em andamento |
| 7 | Insensibilidade | OK | Pendente | Em andamento |
| 8 | Telefone | OK | Pendente | Em andamento |
| 9 | Auto Estrada | OK | Pendente | Em andamento |
| 10 | Viagem Espacial | OK | Pendente | Em andamento |
| 11 | Cavalos | OK | Pendente | Em andamento |
| 12 | Auto Estrada | OK | Pendente | Em andamento |
| 13 | Mini Calculadora | OK | Pendente | Em andamento |
| 14 | Ações da Bolsa | OK | Pendente | Em andamento |
| 15 | OBI | OK | Pendente | Em andamento |
| 16 | Telefone | OK | Pendente | Em andamento |
| 17 | Vestibular | OK | Pendente | Em andamento |


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
| 4 | Monopólio | OK | Pendente | Em andamento |
| 5 | Margaridas | OK | Pendente | Em andamento |
| 6 | Conversa não tão secreta | OK | Pendente | Em andamento |
| 7 | Lobo Mau | OK | Pendente | Em andamento |
| 8 | Autorama | OK | Pendente | Em andamento |
| 9 | Quadrado Mágico | OK | Pendente | Em andamento |
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
| 1 | Bafo | OK | Pendente | Em andamento |
| 2 | Transmissão de Energia | OK | Pendente | Em andamento |
| 3 | Vivo ou Morto | OK | Pendente | Em andamento |
| 4 | Pedido de Desculpas | OK | Pendente | Em andamento |
| 5 | Mini-Poker | OK | Pendente | Em andamento |


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

