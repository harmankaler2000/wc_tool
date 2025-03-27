FROM python:3.10-slim

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt || true
RUN chmod +x /app/main.py

ENTRYPOINT ["python3", "/app/main.py"]
