FROM python:3.9-slim
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
 
COPY app.py app.py
 
EXPOSE 8000
 
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "8000" "app:app" ]