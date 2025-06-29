web: gunicorn koperasi_api.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn koperasi_api.wsgi