FROM python:3.12

WORKDIR /container_app
COPY requirements.txt /container_app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /container_app/requirements.txt

COPY . /container_app/

CMD bash -c "while true; do sleep 1; done"