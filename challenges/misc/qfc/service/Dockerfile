FROM ubuntu:20.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
   apt-get update && apt-get -y dist-upgrade && \
   apt-get install -y lib32z1 xinetd bsdmainutils python3-pip

RUN /usr/bin/python3 -m pip install --no-cache-dir numpy scipy qiskit

RUN useradd -m ctf

WORKDIR /home/ctf

RUN cp -R /usr/lib* /home/ctf

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/*

RUN mkdir /home/ctf/bin && \
    cp /bin/mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin

COPY ./ctf.xinetd /etc/xinetd.d/ctf
COPY ./start.sh /start.sh
RUN echo "Blocked by ctf_xinetd" > /etc/banner_fail

RUN chmod +x /start.sh

COPY ./main.py /home/ctf
COPY ./init.sh /home/ctf
RUN chown -R root:ctf /home/ctf && \
    chmod -R 777 /home/ctf

CMD ["/start.sh"]

EXPOSE 5000
