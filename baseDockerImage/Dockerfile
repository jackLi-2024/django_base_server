FROM centos/python-36-centos7:latest

ADD ./requirements.txt /root/

#RUN yum update -y
#这里是否更新库待定
USER root

#RUN yum install -y vim \
#    && pip3 install -r /root/requirements.txt
RUN pip3 install -r /root/requirements.txt
