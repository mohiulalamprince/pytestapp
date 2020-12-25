FROM python:3.7.6

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "main.py"
ENV FLASK_DEBUG True

RUN mkdir /app
RUN mkdir /app/upload

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["python3.7", "main.py", "--host=0.0.0.0"]

