release: python manage.py migrate

web: gunicorn xray_scan.wsgi --log-file -

python manage.py collectstatic --noinput
python manage.py runserver
