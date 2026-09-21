FROM python:3.12-slim

WORKDIR /app

COPY requirments.txt .

RUN pip install  -r requirments.txt

COPY /app .

EXPOSE 5000
 
CMD ["python3","app.py"]
