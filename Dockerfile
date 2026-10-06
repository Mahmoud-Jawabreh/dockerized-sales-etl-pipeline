FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY pipeline.py .
COPY data ./data

CMD ["python", "pipeline.py"]