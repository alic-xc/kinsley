release: python manage.py migrate
web: gunicorn cocina.wsgi --log-file -
python manage.py collectstatic --noinput
python manage.py runserver
