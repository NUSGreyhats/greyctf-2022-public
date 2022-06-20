FROM php:8.1-apache

COPY app-src/* /var/www/html/

RUN chown -R 0:0 /var/www/html
RUN chmod 755 /var/www/html

COPY flag.txt /flag.txt
COPY readflag.c /readflag.c

RUN gcc /readflag.c -o /readflag
RUN rm /readflag.c

RUN useradd pwn
RUN chown pwn:pwn /readflag
RUN chown pwn:pwn /flag.txt
RUN chmod 4755 /readflag
RUN chmod 0400 /flag.txt

