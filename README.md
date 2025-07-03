# 📊 Análise de Vendas com Curvas Normais

Este projeto tem como objetivo simular um banco de dados de vendas por loja, aplicar conceitos estatísticos (média e desvio padrão) e visualizar as distribuições das vendas com **curvas normais** usando Python e bibliotecas como `pandas`, `matplotlib`, `numpy` e `scipy`.

---

## 🔧 Tecnologias Utilizadas

- Python 3
- SQLite (via `sqlite3`)
- Pandas
- NumPy
- Matplotlib
- SciPy (para curvas normais)

---

## 💡 Objetivo

O projeto simula vendas em 6 lojas de diferentes regiões do Brasil, armazena essas informações em um banco de dados SQLite e realiza a análise estatística para entender o comportamento das vendas, traçando curvas normais para cada loja com base na média e no desvio padrão.

---

## ⚙️ Etapas do Projeto

1. **Criação do Banco de Dados**
   - Tabelas: `loja` e `venda`
   - Dados simulados para 6 lojas

2. **Inserção de Dados**
   - Vendas pares com valores mais altos (ex: R$1000+)
   - Vendas ímpares com valores mais baixos (ex: R$100+)

3. **Leitura e Análise**
   - Leitura dos dados via `pandas`
   - Agrupamento por loja
   - Cálculo de média e desvio padrão

4. **Visualização com Curvas Normais**
   - Para cada loja, foi plotada uma curva normal
   - O eixo X representa o valor da venda
   - O eixo Y representa a densidade de probabilidade
   - Cada curva mostra a distribuição das vendas da loja

---

## 📷 Exemplo de Resultado

https://github.com/RomanoScience/Estat-stica_Python/blob/main/CURVA_NORMAL.png

### Meu Contato
   https://www.linkedin.com/in/ronaldoromanojr/
---

## 📁 Como Executar

1. Clone o repositório:
  https://github.com/RomanoScience?tab=repositories
