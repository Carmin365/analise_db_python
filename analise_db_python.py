# Passo 1: Conectando o banco de dados SQLite e criando uma tabela.

import sqlite3

# Conectar ao banco de dados (ou criar, se não existir)
conexao = sqlite3.connect('dados_vendas.db')

# Criar um cursor
cursor = conexao.cursor()

# Criar uma tabela (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas1 (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    data_venda DATE,
    produto TEXT,
    categoria TEXT,
    valor_venda REAL
)
''')

# Inserir alguns dados
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''')

# Confirmar as mudanças
conexao.commit()


# Passo 2: Explorando e preparando os dados

import pandas as pd

# Carregar os dados em um DataFrame
df_vendas = pd.read_sql_query("SELECT * FROM vendas1", conexao)

# Converter a coluna de data para o formato datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Visualizar os primeiros registros
print(df_vendas.head())


# Passo 3: Analisando dos dados

# Extrair o mês e ano da data de venda
df_vendas['mes_ano'] = df_vendas['data_venda'].dt.to_period('M')

# Vendas totais por categoria
vendas_categoria = df_vendas.groupby('categoria')['valor_venda'].sum().reset_index()

# Vendas totais por mês
vendas_mensal = df_vendas.groupby('mes_ano')['valor_venda'].sum().reset_index()


# Passo 4: Visualizando os dados

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Organização do DataFrame para garantir o bom funcionamento do código
data = {
    'valor_venda': [100, 200, 150, 300],
    'categoria': ['A', 'B', 'A', 'B'],
    'mes_ano': ['2023-01', '2023-02', '2023-03', '2023-04']
}
df_vendas = pd.DataFrame(data)

# Gráfico de vendas totais por categoria
plt.figure(figsize=(10, 6))
sns.barplot(x='valor_venda', y='categoria', data=df_vendas, palette='viridis')
plt.title('Vendas Totais por Categoria')
plt.xlabel('Valor de Vendas (R$)')
plt.ylabel('Categoria')
plt.show()

# Gráfico de vendas mensais
plt.figure(figsize=(12, 6))
sns.lineplot(x='mes_ano', y='valor_venda', data=df_vendas, marker='o')
plt.title('Vendas Mensais')
plt.xlabel('Mês/Ano')
plt.ylabel('Valor de Vendas (R$)')
plt.xticks(rotation=45)
plt.show()


