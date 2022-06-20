## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM ubuntu:20.04 as src

# This is the actual container that runs
FROM redpwn/jail:v0.0.1

ENV JAIL_TIME 60

COPY --from=src / /srv
COPY ./easyoob2 /srv/app/run
COPY ./flag.txt /srv/app/flag.txt
EXPOSE 5000
RUN chmod +x /srv/app/run
