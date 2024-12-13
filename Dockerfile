FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn


COPY . .

EXPOSE 4000

CMD ["gunicorn", "--bind", "0.0.0.0:4000", "app:app"]