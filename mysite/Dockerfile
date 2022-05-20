FROM python:3.8.0
LABEL maintainer="Changseok Lee"

RUN apt-get update \
    && rm -rf /var/lib/apt/lists/*

# WORKDIR /app 으로 변경
WORKDIR /app

# COPY mysite 안에 있는 requiremnts.txt 를 /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Dockerfile 현재 있는 위치에서 .(mysite) Docker container 안에 /app 으로 이동
COPY . /app
RUN chmod 777 /app

EXPOSE 8000
CMD ["/bin/bash", "./script.sh"]