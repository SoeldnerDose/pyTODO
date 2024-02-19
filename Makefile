ENV_FILES := .env
ifeq ($(wildcard .env.local),)
    # If .env.local does not exist, use only .env
else
    ENV_FILES += .env.local
endif

# Load environment variables from .env and .env.local
include $(ENV_FILES)
export $(shell sed 's/=.*//' $(ENV_FILES))

.PHONY: install clean run test

install: venv
	$(VENV)/bin/$(PIP) install -r requirements.txt

venv:
	$(PYTHON) -m venv $(VENV)

clean:
	rm -rf $(VENV) __pycache__ .pytest_cache

run: install
	$(VENV)/bin/$(PYTHON) -m uvicorn main:app

dev: install
	$(VENV)/bin/$(PYTHON) -m uvicorn main:app --reload

install-test:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/$(PIP) install -r requirements-test.txt

lint: install-test
	$(VENV)/bin/$(PYTHON) -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

test: install-test
	$(VENV)/bin/$(PYTHON) -m pytest tests
