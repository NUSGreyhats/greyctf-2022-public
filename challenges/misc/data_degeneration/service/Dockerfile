## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM python:3 AS src

# This is the actual container that runs
FROM redpwn/jail:v0.0.1

ENV JAIL_TIME 2000
ENV JAIL_MEM  20M

COPY --from=src / /srv
COPY ./checker.py /srv/app/run
EXPOSE 5000
RUN chmod +x /srv/app/run
