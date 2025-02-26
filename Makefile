start:
	python3 manage.py runserver --settings=my_store.settings

dev-install:
	pip install -r requirements/dev.txt

dev-m:
	python3 manage.py migrate --settings=my_store.settings

dev-makem:
	python3 manage.py makemigrations --settings=my_store.settings

dev-showm:
	python3 manage.py showmigrations --settings=my_store.settings

dev-sqlm:
	python3 manage.py sqlmigrate $(a) $(m) --settings=my_store.settings

dev-dbshell:
	python3 manage.py dbshell --settings=my_store.settings	

dev-shell:
	python3 manage.py shell --settings=my_store.settings
