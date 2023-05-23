install:
	pip install --upgrade pip
	pip install -r requirements.txt

runWindows:
	python main.py

runMac:
	python3 main.py

allWindows:
	$(MAKE) install
	$(MAKE) runWindows

allMac:
    $(MAKE) install
    $(MAKE) runMac
