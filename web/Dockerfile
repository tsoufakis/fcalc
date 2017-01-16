FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y python-dev python-pip
COPY . /web
WORKDIR /web
RUN pip install .
ENV FLASK_APP=./fcalc/hello.py
CMD flask run --host 0.0.0.0
