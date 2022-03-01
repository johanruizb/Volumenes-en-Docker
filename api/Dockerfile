FROM python:3.8.0-alpine
WORKDIR /code
ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]