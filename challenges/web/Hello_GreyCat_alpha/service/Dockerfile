FROM centos/php-73-centos7

# Add application sources to a directory that the assemble script expects them
# and set permissions so that the container runs without root access
USER 0
ADD app-src /tmp/src
RUN chown -R 1001:0 /tmp/src

COPY flag.txt /flag.txt
COPY readflag.c /readflag.c

RUN gcc /readflag.c -o /readflag
RUN rm /readflag.c

RUN useradd pwn
RUN chown pwn:pwn /readflag
RUN chown pwn:pwn /flag.txt
RUN chmod 4755 /readflag
RUN chmod 0400 /flag.txt

USER 1001

# Install the dependencies
RUN /usr/libexec/s2i/assemble

USER 0

RUN chown -R 0:0 /opt/app-root/src
RUN chmod -R go-w /opt/app-root/src

USER 1001

# Set the default command for the resulting image
CMD /usr/libexec/s2i/run
