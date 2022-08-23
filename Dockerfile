FROM apache/airflow:2.3.3-python3.10

ENV AIRFLOW_HOME=/opt/airflow

ADD requirements.txt $AIRFLOW_HOME/requirements.txt

RUN pip install -r requirements.txt
