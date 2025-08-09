FROM python:3.11-slim

WORKDIR /app

COPY app.py /app/app.py

RUN pip install flask

EXPOSE 8080

CMD ["python", "app.py"]