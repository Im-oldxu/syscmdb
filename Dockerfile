FROM rockylinux:9

RUN yum install gcc gcc-c++ python3 python3-devel libffi-devel -y && \
    yum clean all

ADD  ./requirement.txt /requirement.txt
RUN pip3 install \
    -i https://mirrors.aliyun.com/pypi/simple/ \
    -r /requirement.txt
