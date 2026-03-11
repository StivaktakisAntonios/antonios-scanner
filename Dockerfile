FROM alpine:3

# Antonios Scanner - Simple security demo
RUN apk add --no-cache python3 curl

COPY app.py /app/app.py

WORKDIR /app

CMD ["python3", "app.py"]
