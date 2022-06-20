FROM php:8.1-apache
COPY src/harder.php /var/www/html/index.php
COPY src/flag.txt /flag.txt
COPY src/readflag.c /readflag.c

RUN gcc /readflag.c -o /readflag
RUN rm /readflag.c

# lol
RUN rm /usr/bin/curl

RUN useradd pwn
RUN chown pwn:pwn /readflag
RUN chown pwn:pwn /flag.txt
RUN chmod 4755 /readflag
RUN chmod 0400 /flag.txt
