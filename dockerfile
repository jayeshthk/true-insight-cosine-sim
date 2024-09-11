FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files to disc and to buffer stdout/stderr
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8005 to the outside world
EXPOSE 8005

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8005"]
