# Formatos de Arquivo para Big data

## Parquet

Apache Parquet é um formato de armazenamento de dados orientado a colunas, gratuito e de código aberto.

## Apache ORC

Apache ORC é outro formato de armazenamento de dados orientado a colunas, também gratuito e de código aberto, com muitas semelhanças ao Parquet.

## AVRO

Apache Avro é um formato de serialização de dados voltado para big data e comumente usado em pipelines de dados de streaming.

## Dados

Os dados utilizados estão no diretório files. Os dados de Multas de Estacionamento de Nova York não estão incluídos neste repositório por serem muito grandes. No entanto, eles podem ser baixados no Kaggle: https://www.kaggle.com/datasets/new-york-city/nyc-parking-tickets/.


# Rodando o projeto

## Pipenv
Instale a ferramenta de gerenciamento de pacotes Pipenev (https://pypi.org/project/pipenv/):
```
pip install pipenv
```

Instale as dependências que foram declaradas no Pipfile
```
pipenv install
```