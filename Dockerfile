FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code

COPY . .

EXPOSE 80

# Start the FastAPI app using Uvicorn
CMD ["fastapi", "run", "--host", "0.0.0.0", "--port", "80", "--app", "app"]
