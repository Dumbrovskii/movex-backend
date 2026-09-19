# Base image with Python 3.13 on Debian Bullseye
FROM python:3.13-slim-bullseye

# Copy the uv binary from the official Astral image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set the working directory inside the container
WORKDIR /app

# Add the application source folders to the Python module search path
ENV PYTHONPATH=/app:/app/src

# Copy the application source code into the container
COPY . /app

# Install dependencies using uv based on the uv.lock file
RUN uv sync --locked --no-cache

# Expose and run the FastAPI application using Uvicorn
CMD ["/app/.venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
