FROM python:3.9-alpine
WORKDIR /app
COPY . /app
COPY requirements.txt .
RUN pip3 install -r /requirements.txt
EXPOSE 5000
CMD ["python3", "main.py"]