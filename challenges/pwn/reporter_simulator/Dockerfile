## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM ubuntu:20.04 as src

# This is the actual container that runs
FROM pwn.red/jail

ENV JAIL_TIME 60

COPY --from=src / /srv

COPY ./dist/reporter.o /srv/app/run
COPY ./dist/libc.so.6 /srv/app/libc.so.6
COPY ./dist/ld.so /srv/app/ld.so

COPY ./flag.txt /srv/app/flag.txt
EXPOSE 5000
RUN chmod +x /srv/app/run
