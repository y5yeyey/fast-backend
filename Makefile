SHELL := /bin/bash

clean-venv:
	rm -fr venv

venv: clean-venv
	virtualenv -p python3 venv
	PYTHONPATH=./venv/lib64/python3/dist-packages \
	./venv/bin/python \
	./venv/bin/pip install -r requirements.txt

lint:
	pylint main.py

run-app:
	python3 -m uvicorn main:app --reload
