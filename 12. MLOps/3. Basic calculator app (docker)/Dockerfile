# base image
FROM python:3.11-slim-buster

# workdir
WORKDIR /app

# Install dependencies separately so application files can be copied explicitly.
COPY requirements.txt /app/requirements.txt

#run
RUN pip install -r requirements.txt

# Copy the application and its runtime assets into Flask's expected locations.
COPY app.py /app/app.py
COPY templates/ /app/templates/
COPY static/ /app/static/

#port
EXPOSE 8080

# commands
CMD ["python3", "/app/app.py"]