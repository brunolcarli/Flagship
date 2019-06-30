install_dev:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000 --settings=lisa.settings.common

migrate:
	python manage.py makemigrations --settings=lisa.settings.common
	python manage.py migrate --settings=lisa.settings.common
