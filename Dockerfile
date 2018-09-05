# 基础镜像
FROM ubuntu:16.04

# 支持中文
ENV LANG C.UTF-8

RUN apt-get update && apt-get install -y vim tar wget curl rsync bzip2 iptables tcpdump less telnet net-tools \
lsof psmisc build-essential supervisor libssl-dev software-properties-common git && \
add-apt-repository ppa:deadsnakes/ppa && apt-get update && apt-get install -y python-software-properties \
python3.6 python3.6-dev python3.6-venv && rm -rf /var/lib/apt/lists/*

ADD requirements.txt requirements.txt

RUN wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && ln -s /usr/bin/python3.6 /usr/local/bin/python3 \
&& pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN mkdir /python_demos
ADD . /python_demos

WORKDIR /python_demos