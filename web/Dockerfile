FROM python:2.7
RUN pip install gunicorn
COPY requirements.txt /home/
WORKDIR /home/
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
