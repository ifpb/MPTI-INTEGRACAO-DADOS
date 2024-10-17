import json
import pathlib
import airflow.utils.dates
import requests
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import multiprocessing
multiprocessing.set_start_method('forkserver', force=True)

dag = DAG(
    dag_id="download_rocket_launches",
    description="Download rocket pictures of recently launched rockets.",
    start_date=airflow.utils.dates.days_ago(25),
    schedule_interval="@daily",
)

# task 1: Download launches.
download_launches = BashOperator(
    task_id="download_launches",
    bash_command="curl -o /Users/diegopessoa/airflow-examples/rockets/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",
    dag=dag,
)

# task 2: get pictures.
def _get_pictures():
    # Ensure directory exists
    pathlib.Path("/Users/diegopessoa/airflow-examples/rockets/images").mkdir(
        parents=True, exist_ok=True
    )

    print("Iniciando download")

    # Download all pictures in launches.json
    with open("/Users/diegopessoa/airflow-examples/rockets/launches.json") as f:
        launches = json.load(f)
        image_urls = [launch["image"] for launch in launches["results"]]
        for image_url in image_urls:
            response = requests.get(image_url)
            image_filename = image_url.split("/")[-1]
            target_file = (
                f"/Users/diegopessoa/airflow-examples/rockets/images/{image_filename}"
            )
            with open(target_file, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {image_url} to {target_file}")


get_pictures = PythonOperator(
    task_id="get_pictures", python_callable=_get_pictures, dag=dag
)

# task 3: notify.
notify = BashOperator(
    task_id="notify",
    bash_command='echo "There are now $(ls ~/airflow-examples/rockets/images/ | wc -l) images."',
    dag=dag,
)

# set dependencies.
download_launches >> get_pictures >> notify