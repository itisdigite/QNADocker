# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy backend and frontend code to the container
COPY /qna-backend /app/qna-backend
COPY /qna-frontend /app/qna-frontend

# Install dependencies from the backend
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r /app/qna-backend/requirements.txt

# Expose port 8000 for Flask
EXPOSE 8000

# Command to run the Flask application
CMD ["python", "/app/qna-backend/login_page.py"]
