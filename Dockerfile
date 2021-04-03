FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt 

COPY ./server /app
COPY gunicorn_conf.py /app/

EXPOSE 8000
