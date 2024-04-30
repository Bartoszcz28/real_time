FROM python:3.8-alpine

COPY dashboard/requirements.txt /dashboard/requirements.txt

COPY dashboard/dashboard.py /dashboard/dashboard.py

WORKDIR /dashboard

RUN pip install -r requirements.txt

CMD ["python", "dashboard.py"]
