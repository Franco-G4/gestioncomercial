release: python manage.py migrate --noinput
web: gunicorn GestionComercial.wsgi:application --log-file -
