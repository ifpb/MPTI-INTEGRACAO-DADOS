## Conteúdo

-   [Inspirações](#acknowledgements)
-   [Instalação](#installation)
-   [Referências](#references)
-   [Créditos](#credits)

## Inspirações

-   [Material do Livro Pipelines de Dados com Apache Airflow](https://github.com/BasPH/data-pipelines-with-apache-airflow)

## Instalação

1. Conforme a [documentação](https://airflow.apache.org/docs/apache-airflow/stable/start.html), apenas a instalação via `pip` é oficialmente suportada no momento.

2. A instalação depende da versão do Airflow e da versão do Python. Como exemplo, `AIRFLOW_VERSION=2.10.2` e `PYTHON_VERSION=3.8`.

    ```bash
    pip install "apache-airflow==2.10.2" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.10.2/constraints-no-providers-3.8.txt"
    ```

3. Defina o diretório do Airflow, o padrão é `~/airflow`.

4. Configurando o banco de dados.

    ```bash
    airflow db migrate
    ```

5. Crie o usuário Admin.

    ```bash
    airflow users create --username <usuario> --password <senha> --firstname <nome> --lastname <sobrenome> --role Admin --email <email>
    ```

6. Execute o scheduler.

    ```bash
    airflow scheduler
    ```

7. Em outro terminal ou em segundo plano, execute o servidor web separadamente.

    ```bash
    airflow webserver
    ```

> **Nota**  
> `download_rockets_lauches.py` deve estar dentro de `~/airflow/dags`.

> **Nota**  
> Altere o caminho absoluto no código Python.

> **Nota**  
> Se houver falhas, verifique o código original do [autor](https://github.com/BasPH/data-pipelines-with-apache-airflow/blob/master/chapter02/dags/download_rocket_launches.py).

## Referências

-   Harenslak, B. e Ruiter, J. de (2021) em _Data Pipelines with Apache Airflow_. Shelter Island, NY: Manning Publications Co., pp. 3–33.

## Créditos

-   [@BasPH](https://www.github.com/BasPH)