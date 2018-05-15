#launch with gunicorn
gunicorn -w 1 --access-logfile logfile -b 0.0.0.0:5000 app:app


