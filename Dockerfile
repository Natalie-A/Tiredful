# Stage 1: Build Stage
FROM python:3.14-rc-slim-bookworm AS builder

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./

RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /app/venv \
  && /app/venv/bin/pip install --upgrade pip \
  && /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy source files
COPY . .

# Stage 2: Production Stage
FROM python:3.14-rc-slim-bookworm

# Set working directory
WORKDIR /app/Tiredful-API

# Copy necessary files from build stage
COPY --from=builder /app /app

# Expose the port the app runs on
EXPOSE 8000

# Set non-root user for security (optional)
RUN useradd -m appuser
USER appuser

# Set the PATH to include the virtual environment's bin directory
ENV PATH="/app/venv/bin:$PATH"

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

