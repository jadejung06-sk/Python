
"""
airflow를 사용하는데, 
처음에 pythonOperator로 dataframe을 만든다. 
dataframe이 비어있으면, 멈춘다. 
비어 있지 않으면, 3개의 python Operator로 이루어진 task group이 동시에 진행되고, 
각각 dataframe을 만든 다음에, spark operator로 3개의 dataframe을 합친 결과와 파일을 생성하는 코드를 만들어줘
"""

from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.utils.task_group import TaskGroup
import pandas as pd
import pendulum
import tempfile
import os

def create_dataframe():
    # Simulate DataFrame creation
    df = pd.DataFrame({'data': [1, 2, 3]})  # Replace with actual DataFrame creation logic
    # Save to a temporary file (if needed)
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    df.to_csv(temp_file.name, index=False)
    temp_file.close()
    return temp_file.name

def is_dataframe_empty(file_path):
    # Check if the DataFrame is empty
    df = pd.read_csv(file_path)
    if df.empty:
        return 'end_task'  # Define end_task as the task to run if DataFrame is empty
    else:
        return 'process_group'  # Define process_group as the task group to run if DataFrame is not empty

def create_sub_dataframe(file_path, sub_df_name):
    # Create a sub DataFrame (replace with actual logic)
    df = pd.read_csv(file_path)
    sub_df = df.copy()  # Simulate different processing
    sub_df['sub_data'] = sub_df['data'] * 2  # Example transformation
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv', prefix=f'{sub_df_name}_')
    sub_df.to_csv(temp_file.name, index=False)
    temp_file.close()
    return temp_file.name

def combine_dataframes(file_paths, output_path):
    # Combine DataFrames using Spark (or any other method)
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.appName('CombineDataFrames').getOrCreate()
    
    dfs = [spark.read.csv(path, header=True, inferSchema=True) for path in file_paths]
    combined_df = dfs[0].unionAll(*dfs[1:])
    combined_df.write.csv(output_path, mode='overwrite', header=True)

with DAG(
    dag_id='data_processing_dag',
    start_date=pendulum.datetime(2023, 4, 1, tz='Asia/Seoul'),
    schedule='@daily',
    catchup=False
) as dag:
    
    # Step 1: Create initial DataFrame
    create_df_task = PythonOperator(
        task_id='create_dataframe_task',
        python_callable=create_dataframe,
        do_xcom_push=True
    )

    # Step 2: Check if DataFrame is empty
    check_df_task = BranchPythonOperator(
        task_id='check_dataframe_task',
        python_callable=lambda **kwargs: is_dataframe_empty(kwargs['task_instance'].xcom_pull(task_ids='create_dataframe_task')),
        provide_context=True
    )

    # Define end task
    end_task = DummyOperator(task_id='end_task')

    # Define a task group
    with TaskGroup('process_group') as process_group:
        sub_df_tasks = []
        for sub_df_name in ['sub_df1', 'sub_df2', 'sub_df3']:
            sub_df_task = PythonOperator(
                task_id=f'create_{sub_df_name}_task',
                python_callable=lambda **kwargs: create_sub_dataframe(kwargs['task_instance'].xcom_pull(task_ids='create_dataframe_task'), sub_df_name),
                provide_context=True,
                do_xcom_push=True
            )
            sub_df_tasks.append(sub_df_task)

    # Combine DataFrames with Spark
    combine_dfs_task = SparkSubmitOperator(
        task_id='combine_dataframes_task',
        application='path_to_spark_application',  # Replace with actual path to Spark application
        conn_id='spark_default',  # Replace with your actual Spark connection ID
        # Additional SparkSubmitOperator parameters
        # Arguments to pass to Spark application
    )

    # Set up task dependencies
    create_df_task >> check_df_task
    check_df_task >> [end_task, process_group]
    process_group >> combine_dfs_task
