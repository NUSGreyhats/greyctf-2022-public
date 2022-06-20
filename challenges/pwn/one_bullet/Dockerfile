## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM ubuntu:20.04 as src

# This is the actual container that runs
FROM pwn.red/jail

ENV JAIL_TIME 60

COPY --from=src / /srv

COPY ./dist/one_bullet.o /srv/app/run
COPY ./dist/libc-2.31.so /srv/app/libc-2.31.so
COPY ./dist/ld-2.31.so /srv/app/ld-2.31.so

COPY ./flag.txt /srv/app/flag.txt
EXPOSE 5000
RUN chmod +x /srv/app/run
