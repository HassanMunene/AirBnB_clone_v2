#!/usr/bin/env bash
# Bash script that sets up my web servers for the deployment of web_static

apt-get update
apt-get install -y nginx

mkdir /etc/nginx/html
touch /etc/nginx/html/index.html
echo "Hello Word!" > /etc/nginx/html/index.html
touch /etc/nginx/html/404.html
echo "Ceci n'est pas une page" > /etc/nginx/html/404.html

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello world testing!" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $HOSTNAME;

    root   /etc/nginx/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location =  /404.html {
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart
