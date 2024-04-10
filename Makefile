PYTHON = python3
MANAGE_PY = manage.py

ifdef OS
    ifeq ($(OS),Windows_NT)
        PYTHON = python
    endif
endif

run:
	$(PYTHON) $(MANAGE_PY) run

test:
	poetry run $(PYTHON) $(MANAGE_PY) test
    
migrate:
	$(PYTHON) $(MANAGE_PY) db init
	$(PYTHON) $(MANAGE_PY) db migrate
	$(PYTHON) $(MANAGE_PY) db upgrade

update-migrate:
	$(PYTHON) $(MANAGE_PY) db migrate
	$(PYTHON) $(MANAGE_PY) db upgrade

populate-db:
	$(PYTHON) $(MANAGE_PY) populate

test-cov:
	poetry run pytest --cache-clear --cov=app ./app/test/ > pytest-coverage.txt

active-env:
	poetry shell