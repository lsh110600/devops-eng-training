FROM ubuntu:latest

LABEL maintainer="lsh110600@naver.com"

RUN mkdir -p /tmp
WORKDIR /app

RUN apt-get update
RUN apt-get install pip -y
RUN apt-get install -y git

RUN \
    pip install --upgrade pip &&\
    pip install flask pytest requests &&\
    git clone https://github.com/lsh110600/devops-eng-training.git &&\
    chmod +x start.sh


EXPOSE	80
CMD [ "./start.sh" ]