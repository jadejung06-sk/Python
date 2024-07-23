## dag == work flow
## Operator == 설계도 == 클래스
## Task == 오퍼레이터 통해서 만들어진 객체
## Bash Operator == Shell 명령 수행
## Python Operator == Python 함수 수행
## S3 Operator == AWS 수행
## GCS Operator == google Cloud 수행

## 스케쥴러 : Dag File을 Parsing하여, 문제가 없다면 메타 DB에 정보를 저장하는 역할
## 워커 : 스케쥴러가 정한 시점에 실제 작업을 수행, 메타 DB에 수행 전과 후 결과를 업데이트



import datetime
import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id = "example_bash_operator", ## ID in DAGs == File name과 일치하는 것이 나중을 위해 편함 
    schedule = "0 0 * * *", # 시 분 Cron Expression
    start_date = pendulum.datetime(2023, 3, 1, tz = "Asia/Seoul"),
    catchup = False, # 과거 누락된 기간을 한꺼번에 돌리는 기능으로, 2023년 1월 1일 ~ 2023년 2월말까지를 채워 넣어서, 보통 사용 안하는 기능 
    # dagrun_timeout = datetime.timedelta(minutes=60), # 60분 돌아가면 실패하는 기능
    tags = ["example", "example2"],
    # params = {"example_key": "example_value"}, # 공통적으로 사용할 변수를 사용하는 기능
) as dag:
    bash_t1 = BashOperator( #객체 이름
        task_id = "bash_t1", # Graph에 존재하는 이름으로 객체 이름과 일치하는 것이 나중을 위해 편함
        bash_command = "echo whoami",
    )
    
    bash_t2 = BashOperator( #객체 이름
        task_id = "bash_t2", # Graph에 존재하는 이름으로 객체 이름과 일치하는 것이 나중을 위해 편함
        bash_command = "echo $HOSTNAME",
    )
    
    bash_t1 >> bash_t2
    
    
    
## yaml 파일을 vi로 읽으면, Volumns을 확인할 수 있음
## /dags (wsl Volumn 영역) : 연결해라  /opt/airflow/dags (Docker Container Volumn 영역)
## ${AIRFLOW_PROJ_DIR:-.} == AIRFLOW_PROJ_DIR 값이 있으면 출력하고 없으면 . 을 출력하라.
## DAG는 처음에 Pause 상태로 올라오기 때문에 unpause가 필요함
## Log Tab 통해서 결과를 확인할 수 있음 Output : 부분에서 확인 가능
