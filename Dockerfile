FROM jupyter/pyspark-notebook:notebook-7.0.2
USER root

RUN apt-get update && \
    apt-get install -y curl vim wget git netcat graphviz && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip setuptools wheel

RUN pip install --no-cache-dir tensorflow==2.15.0 torch==2.2.0 && \
    pip install --no-cache-dir pylatexenc==2.10 ipywidgets==8.1.0 flask==3.0.1 pydot==2.0.0 && \
    pip install --no-cache-dir pandas==1.5.3 numpy==1.24.4 scipy==1.11.2 matplotlib==3.7.2 sympy==1.12 seaborn==0.12.2 && \
    pip install --no-cache-dir kafka-python==2.0.2 confluent_kafka==2.3.0 && \
    fix-permissions "/home/${NB_USER}" 

RUN pip install psycopg2-binary==2.9.9

RUN wget https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz && \
    tar -xzf kafka_2.13-3.7.0.tgz && \
    mv kafka_2.13-3.7.0 /home/jovyan/kafka

RUN rm -f /home/jovyan/kafka_2.13-3.7.0.tgz

COPY trigger_stream.sh /home/jovyan/trigger_stream.sh
RUN sed -i 's/\r$//' /home/jovyan/trigger_stream.sh

USER ${NB_USER}

WORKDIR /home/jovyan/notebooks

CMD ["/bin/bash", "-c", "/home/jovyan/trigger_stream.sh && start-notebook.sh --NotebookApp.token='root' --NotebookApp.allow_origin='*'"]