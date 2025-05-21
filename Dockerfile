# Use official Python runtime as a parent image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Run the Gunicorn server with collectstatic at startup
CMD python manage.py collectstatic --noinput && gunicorn food_track.wsgi:application --bind 0.0.0.0:8000
