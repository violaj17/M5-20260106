FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install -r docker/requirements.txt
ENTRYPOINT ["python3", "scripts/app_refactored.py"]
