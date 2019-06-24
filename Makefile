install_dev:
	pip install -r requirements/development.txt

run:
	python manage.py runserver 0.0.0.0:8000
