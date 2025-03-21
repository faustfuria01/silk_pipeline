FROM python:3.10-slim

WORKDIR /app

# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the dependencies and install them
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the whole project
COPY . .

EXPOSE 8000

CMD ["python", "main.py"]
