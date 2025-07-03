import sqlite3
import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
# funcao para criar banco de dados caso vc nao tenha um banco de dados no seu computador
venda = []
def criar_banco (nome_do_banco):
    # criacao de um objeto para criar um banco de dados chamado PROJETO_5
    banco = sqlite3.connect("PROJETO_6")
    return banco
# funcao para manipular o banco de dados criado ou seja precisamos atribuir o nome do banco de dados nessa funcao
def manipular (banco):
    criar = banco.cursor()
    criar.execute(''' create table IF NOT EXISTS loja(
                     id_loja integer primary key,
                     nome_loja text,
                     regiao text) 
                  ''')
    
    criar.execute(''' CREATE TABLE IF NOT EXISTS venda(
                     id_venda integer primary key,
                     nome_loja text,
                     id_loja integer,
                     valor_venda real,
                     FOREIGN KEY (id_loja) REFERENCES loja (id_loja))
                  ''')
    banco.commit()
# funcao para inserir dados nas tabelas criadas
def inserir_dados(banco):
    inserir = banco.cursor()
    inserir.execute('DELETE FROM venda')
    inserir.execute('DELETE FROM loja')
    inserir.executemany(''' INSERT INTO loja (id_loja,nome_loja,regiao) values (?,?,?)''',
                       [(1, 'Loja A', 'Norte'),
                        (2, 'Loja B', 'Sul'),
                        (3, 'Loja C', 'Sudeste'),
                        (4, 'Loja d', 'Norte'),
                        (5, 'Loja e', 'Sul'),
                        (6, 'Loja r', 'Sudeste') ]
                        )
    for i in range(1,101):
        if i%2==0:
            id_venda = i
            id_loja = (i%6) +1
            nome_loja = f'loja{chr(64+id_loja)}'
            valor_venda = 1000 +(i%500)
            venda.append((id_venda,id_loja,nome_loja,valor_venda))
            inserir.executemany('INSERT OR REPLACE INTO venda (id_venda,id_loja,nome_loja,valor_venda) VALUES (?,?,?,?)',venda)
        else:
            id_venda = i
            id_loja = (i%6) +1
            nome_loja = f'loja{chr(64+id_loja)}'
            valor_venda = 100 +(i%50)
            venda.append((id_venda,id_loja,nome_loja,valor_venda))
            inserir.executemany('INSERT OR REPLACE INTO venda (id_venda,id_loja,nome_loja,valor_venda) VALUES (?,?,?,?)',venda)
    banco.commit()
# agora definir a funcao main() que realizara todo o processo de ordenar todos as funções defindas
def main():
    conexao = criar_banco("PROJETO_6.db")
    manipular(conexao)
    inserir_dados(conexao)
    print("Banco de dados criado com sucesso")
    # CMD read_sql_query é um comando de leitura de banco de dados SQL no qual pega os dados de uma coluna e copia para ser manipulado em ptyhon
    # estou selecionado todas as tabelas chamadas vendas do banco de dados 
    df = pd.read_sql_query('SELECT*FROM venda',conexao)
    #CMD df.head() que consulta os dados da tabela do data frame definido na linha de codigo acima no caso coluna venda
    conexao.close()
    return df
if __name__ == '__main__':
    main() 
# Próxima etapa é utilizar cmd que expressão valores como soma e média onde é criado um outro dataframe
# chamando a funcao main() que retorna o objeto data frame
df = main()
# Irei tracar a Curva normal dos dados para analisar se o valores estão abaixo, próximo ou acima da media usando simetria a direita, central e a esquerda
# 1° Logo o primeiro passo é calcular a media de cada loja para saber estabelecer o centro da curva normal
media_vendas = (df.groupby("nome_loja")["valor_venda"].mean())
print(f"valores da média dos grupos são: {media_vendas}")
# 2° Segundo passo é determinar o desvio padrão que define a largura da curva que no qual representa o quão os dados varias em torno da media
desvio_padrao = df.groupby("nome_loja")["valor_venda"].std()
print(f" desvio padrão de cada loja são: {desvio_padrao}")
# 3° Passo é definir a "LARGURA" da curva normal ou seja incluir todos os dados distantes baixou ou acima da média e próximo dessa
# 3.1° assim o eixo x é definifo como e o cmd linspace pega valores igualmente espaçados entre a e b
# 4° passo definir a função de densidade de probabilidade (PDF)
# Como são mais de uma loja utilizarei um laço for para anexar os valores da media e desvio padrão corresponde a cada loja
# como tanto meu desvio padrão e media estão associado com nome_loja assim irei pecorrer cada nome de loja um a um usando o index
fig, axs = plt.subplots(2, 3, figsize=(15, 8))
axs = axs.flatten()
for i, nome_loja in enumerate(media_vendas.index):
    media = media_vendas[nome_loja]
    desvio = desvio_padrao[nome_loja]
    x= np.linspace(media - 4*desvio, media + 4*desvio,100)
    y = norm.pdf(x,media,desvio)
    axs[i].plot(x, y)
    axs[i].set_title(nome_loja)
    axs[i].set_xlabel("Valor da Venda")
    axs[i].set_ylabel("Densidade")
    axs[i].grid(True)

plt.tight_layout()
plt.show()