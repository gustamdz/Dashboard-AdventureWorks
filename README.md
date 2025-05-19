# Dashboard de Vendas - AdventureWorks

Este projeto consiste em um dashboard interativo desenvolvido com Streamlit, utilizando dados do banco AdventureWorks2022 hospedado em um servidor SQL Server. O objetivo é visualizar de forma clara e funcional as métricas de vendas da empresa, como:

- Total de vendas ao longo do tempo

- Desempenho por produto e por região

- Filtros dinâmicos de data, produto e região

### 📋 Pré-requisitos

- IDE recomendada: Visual Studio Code (VS Code)
- Python 3.8 ou superior **ou** Anaconda (recomendado)
- Dependências (caso use Python puro):
  - pandas
  - plotly
  - streamlit
  - sqlalchemy
  - urllib
- Microsoft SQL Server Management Studio (SSMS)
- Banco de dados AdventureWorks2022

### 🔧 Instalação

1. Baixe ou clone o repositório do projeto.
2. Caso utilize Python puro, instale as dependências acima com:
   - "pip install pandas plotly streamlit sqlalchemy urllib3"
4. Caso utilize Anaconda, as dependências já vêm instaladas por padrão.
5. Instale o Microsoft SQL Server Management Studio e configure o banco AdventureWorks2022.
   - Link do Banco [AdventureWorks](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms)
6. Dentro da pasta do projeto, execute:

## ⚙️ Executando

Ápos ter executado o passo a passo acima, faça:
  - Abra o SSMS
  - Restaure o banco "AdventureWorks2022"
  - Dentro do código, mude as configurações de conexão para conectar ao seu SQL Server
  - E no final, insira esse comando no Bash: "streamlit run dash_vendas.py"

Esse comando irá abrir uma janela no navegador, onde terá o Script rodando 100% funacional

## 🛠️ Construído com

* [Anaconda](https://www.anaconda.com/) - Interpretador usado
* [Microsoft SQL Server Management Studio](https://learn.microsoft.com/en-us/ssms/download-sql-server-management-studio-ssms) - Servidor de Banco de Dados
* [AdventureWorks](https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure?view=sql-server-ver16&tabs=ssms) - Banco usado



## ✒️ Autores

* **Gustavo Gomes** - *Trabalho Inicial* - [Desenvolvedor](https://github.com/gustamdz)

---
⌨️ com ❤️ por [Gustavo Gomes](https://github.com/gustamdz) 😊
