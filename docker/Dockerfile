FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r docker/requirements.txt

# Run your script from the correct location
ENTRYPOINT ["python3", "scripts/app_refactored.py"]

