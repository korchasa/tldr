#!/bin/bash

# Script to run tokenization testing in Docker container

# Check if API key is set
if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "Error: OPENROUTER_API_KEY environment variable is not set"
    echo "Please set it with: export OPENROUTER_API_KEY='your-api-key-here'"
    exit 1
fi

# Create results directory if it doesn't exist
mkdir -p results

# Build Docker image
echo "Building Docker image..."
docker build -t openrouter-token-tester .

# Run container
echo "Running tokenization tests..."
docker run --rm \
    -e OPENROUTER_API_KEY="$OPENROUTER_API_KEY" \
    -e RESULTS_DIR=/app/results \
    -v "$(pwd)/results:/app/results" \
    openrouter-token-tester

echo "Tests completed."
