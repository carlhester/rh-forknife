#Tools

## app: Python flask
## data: https://fortnitetracker.com/site-api
## css: bulma
## web: nginx proxy to gunicorn
## hosting: aws lightsail


## gunicorn
gunicorn -w 1 --access-logfile logfile -b 0.0.0.0:5000 app:app


## nginx proxy config stanza in /etc/nginx/nginx.conf:
    server {
        listen       80 default_server;
        #listen       [::]:80 default_server;
        server_name  1.2.3.4 (public ip addr);
        root         /usr/share/nginx/html;

        location / {
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $remote_addr;
            proxy_set_header X-Forwarded-Host $remote_addr;
            proxy_pass http://127.0.0.1:5000;
        }
