FROM python:2.7
COPY requirements.txt /home/
WORKDIR /home/
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code
