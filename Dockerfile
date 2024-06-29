FROM python:3.8
RUN mkdir /app
WORDIR /app
COPY . .
CMD ["python3","add.py"]
