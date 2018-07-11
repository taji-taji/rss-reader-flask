FROM python:3.6

MAINTAINER Yutaka Tajika <y.tajika529@gmail.com>

USER root
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y  vim \
                        sudo \
                        python3-dev \
                        zlib1g-dev \
                        libsqlite3-dev \
                        libreadline6-dev \
                        libgdbm-dev \
                        libbz2-dev \
                        tk-dev

RUN pip install virtualenv \ 
                pipenv

COPY * /root/opt/
WORKDIR /root/opt
RUN pipenv install --system