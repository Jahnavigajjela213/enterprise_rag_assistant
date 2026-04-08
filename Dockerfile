FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (needed for vector db/Huggingface processing)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code
COPY . .

# Ensure start script is executable
RUN chmod +x start.sh

# Run the single startup script
CMD ["./start.sh"]
