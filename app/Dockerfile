FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN pip3 install psycopg2-binary
CMD ["python3", "main.py"]