FROM python:3.9-slim
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
 
COPY . .
 
EXPOSE 8000

RUN python -m pip show uvicorn

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# Added for debugging to see the contents of the app directory (already checked so no longer needed)
# CMD ["sh", "-c", "ls -l /app && uvicorn app:app --host 0.0.0.0 --port 8000"]
