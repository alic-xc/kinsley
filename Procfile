release: python xray_scan/manage.py migrate
web: gunicorn xray_scan.xray_scan.wsgi --log-file -
python xray_scan/manage.py collectstatic --noinput
python xray_scan/manage.py runserver
