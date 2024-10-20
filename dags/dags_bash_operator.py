from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami",
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME",
    )

    bash_t1 >> bash_t2 # task 의 수행 순서 관계
    # 여기서 bash_command 는 우리가 어떤 쉘 스크립트를 수행할지에 대해 작성하는 것이다.