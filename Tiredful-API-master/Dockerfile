FROM alpine:3.20
LABEL maintainer="jsvazic@gmail.com"

COPY . /app/

# Install the required packages
RUN apk add --no-cache \
    python3 \
    python3-dev \
    py3-pip \
    build-base \
    ca-certificates

# Create a virtual environment and install requirements
RUN python3 -m venv /app/venv \
  && /app/venv/bin/pip install --upgrade pip \
  && /app/venv/bin/pip install --no-cache-dir -r /app/requirements.txt

RUN addgroup --gid 1001 pythongroup && \
    adduser --uid 1001 --ingroup pythongroup --system --no-create-home pythonuser

WORKDIR /app/Tiredful-API

USER pythonuser

EXPOSE 8000

# Use the virtual environment to run your app
CMD ["/app/venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]

