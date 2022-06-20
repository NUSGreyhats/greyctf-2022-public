## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM ubuntu:16.04 as src_old
RUN apt-get -y update
RUN apt-get install -y libstdc++6

# This is the actual container that runs
FROM pwn.red/jail

ENV JAIL_TIME 60
ENV JAIL_TMP_SIZE 1000

COPY --from=src_old / /srv

# RUN mkdir /srv/app && ln -s /bin/sh /srv/app/run
# COPY ./dist/ld-2.23.so /srv/app/ld-2.23.so
# COPY ./dist/libc-2.23.so /srv/app/libc-2.23.so
# COPY ./dist/manipulation.o /srv/app/manipulation.o
# COPY ./dist/libstdc++.so.6 /srv/app/libstdc++.so.6
# COPY ./dist/libgcc_s.so.1 /srv/app/libgcc_s.so.1
# COPY ./dist/libm-2.31.so /srv/app/libm-2.31.so

COPY ./dist/manipulation.o /srv/app/run
COPY ./dist/ld-2.23.so /srv/app/ld-2.23.so
COPY ./dist/libc-2.23.so /srv/app/libc-2.23.so

COPY ./flag.txt /srv/app/flag.txt
EXPOSE 5000
RUN chmod +x /srv/app/run
