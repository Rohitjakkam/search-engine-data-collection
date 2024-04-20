FROM python:3.9.14-slim-bullseye

# Set environment variables
ENV AWS_ACCESS_KEY_ID=your_access_key_id
ENV AWS_SECRET_ACCESS_KEY=your_secret_access_key
ENV AWS_BUCKET_NAME=your_bucket_name

COPY . /searchengine

WORKDIR /searchengine

RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8080

CMD ["python","app.py"]