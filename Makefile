install_dev:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000 --settings=server.settings.common

migrate:
	python manage.py makemigrations --settings=server.settings.common
	python manage.py migrate --settings=server.settings.common
