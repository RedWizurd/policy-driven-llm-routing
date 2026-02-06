PYTHON ?= python3
VENV ?= .venv
PIP := $(VENV)/bin/pip
PY := $(VENV)/bin/python

.PHONY: setup check run

setup:
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

check:
	test -f routing_policy.json || cp routing_policy.example.json routing_policy.json
	$(PY) validate_routing_policy.py routing_policy.json

run:
	test -f routing_policy.json || cp routing_policy.example.json routing_policy.json
	$(PY) router.py --mode chat --input "hello" --policy routing_policy.json
