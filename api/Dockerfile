FROM python:3.7.2
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
CMD [ "uwsgi", "app.ini" ]