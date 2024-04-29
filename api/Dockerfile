FROM python:3.8-alpine

COPY api/requirements.txt /api/requirements.txt
# COPY api/api_starter.sh /api/api_starter.sh
COPY api/main.py /api/main.py

WORKDIR /api

RUN pip install -r requirements.txt

# RUN chmod +x /api/api_starter.sh

# CMD ["./api_starter.sh"]
CMD ["python", "main.py"]
