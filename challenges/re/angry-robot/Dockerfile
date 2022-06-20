# welcome-ctf pwn jail
## Based on https://github.com/redpwn/jail
# Rudimentary per-connection python runner based on the Pwn Dockerfile template

# This is the source filesystem that we copy important runtime files from
FROM python:3 AS src
# Install additional dependencies here e.g. 32-bit runtime (lib32z1)

# This is the actual container that runs
FROM redpwn/jail:latest

# Kill each connection after 600 wall seconds (more options in https://github.com/redpwn/jail#configuration-reference)
ENV JAIL_TIME 600

# Copy the entire python filesystem from src to here
COPY --from=src / /srv/
RUN rm -rf /srv/tmp

# Copy over files
COPY . /srv/app

COPY ./server.py /srv/app/run
EXPOSE 5000
RUN chmod +x /srv/app/run

# # runner.sh will be the shell script that actually runs per connection
# COPY run /srv/app/run
