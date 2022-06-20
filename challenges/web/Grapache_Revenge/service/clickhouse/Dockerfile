FROM clickhouse/clickhouse-server

ENV CLICKHOUSE_USER=grey_user
ENV CLICKHOUSE_PASSWORD=grey_password_eaa75d0a
ENV CLICKHOUSE_DB=grey_database
ENV CLICKHOUSE_DEFAULT_ACCESS_MANAGEMENT=1

RUN apt update && apt install -y nginx

COPY flag.txt /var/www/html/index.html

COPY default /etc/nginx/sites-available/default
