# greyctf pwn jail
## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

FROM python:3 AS src

# This is the actual container that runs
FROM redpwn/jail:latest

ENV JAIL_TIME 300

# Copy the entire python filesystem from src to here
COPY --from=src / /srv/
COPY ./main.py /srv/app/run
COPY ./complex.py /srv/app/complex.py
EXPOSE 5000
RUN chmod +x /srv/app/run
