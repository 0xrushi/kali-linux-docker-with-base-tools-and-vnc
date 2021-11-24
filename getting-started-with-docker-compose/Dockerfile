FROM python:3.7-alpine
WORKDIR /CODE
RUN apk add --no-cache gcc musl-dev linux-headers firefox chromium
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
