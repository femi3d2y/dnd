FROM python:3.6.9


WORKDIR /opt/flask-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ../scripts/insert.sh .

RUN insert.sh

ENTRYPOINT ["/usr/local/bin/python", "app.py"]

COPY . .
