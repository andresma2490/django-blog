FROM python:3
ENV PYTHONUNBUFFERED=1

WORKDIR /code
COPY . /code/

RUN apt-get update -y && \
    apt-get upgrade -y && \
    curl -sL https://deb.nodesource.com/setup_lts.x | bash - &&\
    apt-get install -y nodejs &&\
    rm -rf /var/lib/apt/lists/*    

RUN pip install -r requirements.txt