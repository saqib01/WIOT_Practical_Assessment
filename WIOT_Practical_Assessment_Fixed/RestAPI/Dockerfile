# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py /app/

# Install dependencies
RUN pip install --no-cache-dir flask mysql-connector-python

# Expose port 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
