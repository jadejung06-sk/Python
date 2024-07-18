'''
chatgpt 3.5를 활용해서, 하기와 같은 질문으로 만든 일반 코드
airflow 활용해서
매일 오전 6시에 진행하는 스케쥴러를 만들건데, 
PICKLE 형태의 데이터를 두고, 
데이터가 추가되면 이메일을 보내는 API를 활용해서 메일을 보내주고, 
아니면 그냥 아무것도 실행하지 않는 python code로 알려줘
'''

from datetime import datetime, timedelta
import pickle
import requests  # 이메일 보내기 API 호출을 위한 패키지
from airflow import DAG
from airflow.operators.python_operator import PythonOperator


def send_email_on_data_update():
    # PICKLE 파일 경로 설정
    pickle_file_path = '/path/to/your/data.pickle'

    try:
        # 이전 데이터 로드
        with open(pickle_file_path, 'rb') as f:
            previous_data = pickle.load(f)
    except FileNotFoundError:
        previous_data = []

    # 새로운 데이터가 추가되었는지 확인하는 예시
    new_data = ['new_data1', 'new_data2']  # 예시로 새로운 데이터 추가

    if new_data != previous_data:
        # 데이터가 업데이트되었으므로 이메일 보내기 API 호출 예시 (실제로는 사용하는 이메일 서비스의 API를 호출해야 합니다)
        email_api_url = 'https://api.example.com/send_email'
        email_content = {
            'to': 'recipient@example.com',
            'subject': 'Data Updated in PICKLE File',
            'body': 'New data has been added or modified in the PICKLE file.',
        }
        
        response = requests.post(email_api_url, json=email_content)

        if response.status_code == 200:
            print("Email sent successfully!")
        else:
            print(f"Failed to send email. Status code: {response.status_code}")

        # PICKLE 파일 업데이트
        with open(pickle_file_path, 'wb') as f:
            pickle.dump(new_data, f)
    else:
        print("No new data added. Nothing to email.")



# DAG 정의
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 7, 1, 6, 0, 0),  # 시작 날짜와 시간 설정 (매일 오전 6시)
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'email_on_pickle_update',  # DAG의 이름
    default_args=default_args,
    description='A daily scheduler with email alert on PICKLE data update',
    schedule_interval=timedelta(days=1),  # 매일 실행되도록 설정
)

# PythonOperator를 사용하여 PICKLE 파일 업데이트 확인 작업을 DAG에 추가
check_pickle_update_task = PythonOperator(
    task_id='check_pickle_update_task',
    python_callable=send_email_on_data_update,
    dag=dag,
)
