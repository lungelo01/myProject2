# Use an official Python runtime
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# add README.md
git add README.md
git commit -m "Add project README"

# Port and entrypoint
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
