app: Python flask

data: https://fortnitetracker.com/site-api

css: bulma

web: nginx proxy to gunicorn

hosting: aws lightsail


launched with gunicorn
gunicorn -w 1 --access-logfile logfile -b 0.0.0.0:5000 app:app


