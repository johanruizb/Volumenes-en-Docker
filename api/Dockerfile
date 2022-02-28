FROM python:3.8.0-alpine
ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0"]
