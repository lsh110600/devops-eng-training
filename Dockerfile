FROM ubuntu:latest

LABEL maintainer="lsh110600@naver.com"

RUN mkdir -p /tmp
WORKDIR /tmp

RUN apt-get update
RUN apt-get install pip -y
RUN apt-get install -y git

RUN \
    pip install --upgrade pip &&\
    pip install flask pytest requests &&\
    git clone https://github.com/lsh110600/devops-eng-training.git
    
RUN cd /tmp/devops-eng-training
WORKDIR /tmp/devops-eng-training
RUN chmod +x start.sh


EXPOSE	8080
CMD [ "./start.sh" ]
