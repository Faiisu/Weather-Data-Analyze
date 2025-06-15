from prefect import flow, task
import subprocess

@task
def ingestion_task():
    subprocess.run(["python", "src/ingestion.py"], check=True)

@task
def format_task():
    subprocess.run(["python", "src/format.py"], check=True)

@task
def cleaning_task():
    subprocess.run(["python", "src/cleaning.py"], check=True)

@flow
def weather_pipeline():
    ingestion_task()
    format_task()
    cleaning_task()

if __name__ == "__main__":
    weather_pipeline()