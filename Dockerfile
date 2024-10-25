# Stage 1: Build Stage
FROM python:3.10-slim AS builder

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file first to leverage caching
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Stage 2: Production Stage
FROM alpine:latest

# Install only the necessary runtime packages
RUN apk add --no-cache \
    python3 \
    ca-certificates

# Set the working directory in the production container
WORKDIR /app

# Copy the built application from the builder stage
COPY --from=builder /app /app

# Create a user and group for running the application
RUN addgroup -S pythongroup && \
    adduser -S pythonuser -G pythongroup

# Switch to the non-root user
USER pythonuser

# Expose the application port
EXPOSE 8000

# Run the application using the system's Python
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

