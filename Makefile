admin:
	python ./manage.py createsuperuser

migrate:
	python ./manage.py makemigrations
	python ./manage.py migrate

runserver:
	python ./manage.py runnserver

requirements:
	pip freeze >requirements.txt
