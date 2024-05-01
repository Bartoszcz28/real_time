FROM python:3.8-alpine

RUN apk update && \
    apk add --no-cache build-base openblas-dev freetype-dev pkgconfig

ENV BLAS=/usr/lib/libopenblas.so LAPACK=/usr/lib/libopenblas.so

RUN pip install numpy dash pandas psycopg2-binary

# COPY dashboard/requirements.txt /dashboard/requirements.txt


COPY dashboard/table.py /dashboard/table.py

WORKDIR /dashboard

CMD ["python", "table.py"]
