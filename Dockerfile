FROM python:3.8-slim

WORKDIR /app

COPY app.py .

ENTRYPOINT ["python", "app.py"]
