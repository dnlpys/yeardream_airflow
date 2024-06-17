from airflow import DAG
import datetime
import pendulum
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from airflow.decorators import dag

@dag(dag_id="dags_bash_operator_decorator",
     start_date=datetime.datetime(2024, 6, 1, tz="Asia/Seoul"),
     schedule="0 13 * * 5#2",
     catchup=False,
     tag=['homework'])

def dags_bash_operator_decorator():
    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command="echo whoami"
    )

    bash_t2 = BashOperator(
        task_id="bash_t2",
        bash_command="echo $HOSTNAME"
    )

    bash_t1 >> bash_t2

dags_bash_operator_decorator()


# with DAG(
#     dag_id="dags_bash_operator",
#     schedule="0 0 * * *",
#     start_date=pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
#     catchup=False
# ) as dag:
#     bash_t1 = BashOperator(
#         task_id="bash_t1",
#         bash_command="echo whoami",
#     )
#
#     bash_t2 = BashOperator(
#         task_id="bash_t2",
#         bash_command="echo $HOSTNAME",
#     )








