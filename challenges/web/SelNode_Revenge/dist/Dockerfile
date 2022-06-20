from selenium/standalone-chrome:latest

USER root

COPY flag /flag

RUN chmod ugo+x /flag && chmod ugo-r /flag

USER seluser
