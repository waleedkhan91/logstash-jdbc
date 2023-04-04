FROM python:3.8-slim-buster

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyodbc

ADD test.py /

CMD [ "python", "./test.py" ]