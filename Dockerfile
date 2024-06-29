FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY . .
CMD ["python3","add.py"]
