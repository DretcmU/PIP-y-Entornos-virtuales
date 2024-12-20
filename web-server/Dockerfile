FROM python:3.12

WORKDIR /container_web
COPY requirements.txt /container_web/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /container_web/requirements.txt

COPY . /container_web/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]