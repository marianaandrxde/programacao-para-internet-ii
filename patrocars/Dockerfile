FROM bitnami/python:3.9.5

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD uvicorn main:app --reload --host 0.0.0.0 --port ${PORT:-8000}
