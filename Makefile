install:
	pip install --upgrade pip
	pip install -r requirements.txt

runWindows:
	python manage.py runserver 0.0.0.0:8080

runMac:
	python3 manage.py runserver 0.0.0.0:8080

allWindows:
	$(MAKE) install
	$(MAKE) runWindows

allMac:
	$(MAKE) install
	$(MAKE) runMac

