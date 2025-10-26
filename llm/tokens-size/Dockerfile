FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY token_test.py .

# Create results directory
RUN mkdir -p /app/results

# Set environment variable for results output
ENV RESULTS_DIR=/app/results

# Run the script
CMD ["python", "token_test.py"]
