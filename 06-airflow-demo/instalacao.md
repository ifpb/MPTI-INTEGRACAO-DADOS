## Conteúdo

-   [Inspirações](#acknowledgements)
-   [Instalação](#installation)
-   [Referências](#references)
-   [Créditos](#credits)

## Inspirações

-   [Material do Livro Pipelines de Dados com Apache Airflow](https://github.com/BasPH/data-pipelines-with-apache-airflow)

## Instalação via Docker

1. Rode o comando de inicialização para preparar o ambiente:
```bash
docker compose up airflow-init
```

2. Uma vez concluída a inicialização, rode os serviços
```bash
docker compose up -d
```

3. Acesse http://localhost:8080 com usuário `airflow` e senha `airflow`.

## Referências

-   Harenslak, B. e Ruiter, J. de (2021) em _Data Pipelines with Apache Airflow_. Shelter Island, NY: Manning Publications Co., pp. 3–33.

## Créditos

-   [@BasPH](https://www.github.com/BasPH)