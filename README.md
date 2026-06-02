# online-shoppers-project
Project DataEng
# Online Shoppers Project

## Descrição do Projeto

Este projeto foi desenvolvido no âmbito da unidade curricular de Engenharia de Dados.

O objetivo principal foi aplicar técnicas de limpeza, transformação e ingestão de dados utilizando um dataset real contendo informação sobre intenções de compra de utilizadores numa plataforma de comércio eletrónico.

Foi utilizado o dataset **Online Shoppers Purchasing Intention Dataset**, disponibilizado pela UCI Machine Learning Repository.

## Tecnologias Utilizadas

* Python
* Pandas
* MongoDB
* PyMongo
* Docker
* Docker Compose
* Git
* GitHub

## Estrutura do Projeto

```text
online-shoppers-project/

├── raw/              # Dataset original (dados sujos)
├── cleaned/          # Dataset após limpeza
├── scripts/          # Scripts Python do projeto
├── README.md
├── requirements.txt
├── docker-compose.yml
└── .gitignore
```

## Limpeza dos Dados

Durante o desenvolvimento do projeto foram realizadas várias tarefas de preparação e limpeza dos dados, incluindo:

* Identificação e tratamento de valores em falta;
* Normalização de valores categóricos;
* Limpeza e padronização dos nomes das colunas;
* Conversão de valores booleanos para um formato consistente;
* Preparação dos dados para armazenamento em base de dados.

## Processo ETL

O projeto segue um processo ETL (Extract, Transform, Load):

1. Extração dos dados a partir do ficheiro CSV original;
2. Transformação e limpeza dos dados utilizando Python e Pandas;
3. Carregamento dos dados limpos para MongoDB através da biblioteca PyMongo.

## Execução do Projeto

### Iniciar o MongoDB

```bash
docker compose up -d
```

### Executar a limpeza dos dados

```bash
python scripts/clean_data.py
```

### Carregar os dados para a base de dados

```bash
python scripts/load_to_mongodb.py
```

## Dataset Utilizado

Online Shoppers Purchasing Intention Dataset

Fonte:
https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset

## Conclusão

Este projeto permitiu aplicar conceitos fundamentais de Engenharia de Dados, incluindo limpeza de dados, desenvolvimento de pipelines ETL, utilização de Docker para orquestração de serviços e armazenamento de informação em MongoDB.
