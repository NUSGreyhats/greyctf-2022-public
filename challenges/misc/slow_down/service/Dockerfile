## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM ubuntu:20.04 as src

# This is the actual container that runs
FROM redpwn/jail:v0.0.1

ENV JAIL_TIME 2000
ENV JAIL_MEM  20M

COPY --from=src / /srv
COPY ./chall /srv/app/run
EXPOSE 5000
RUN chmod +x /srv/app/run
