# CI
ifeq ($(GENKAIERA_IS_CI),"1")
    ifneq (,$(wildcard ./.env.ci))
        include .env.ci
        export
    else
        $(error ".env.ci file is missing")
    endif

# TEST
else ifeq ($(GENKAIERA_IS_TEST),"1")
    ifneq (,$(wildcard ./.env.test))
        include .env.test
        export
    else
        $(error ".env.test file is missing")
    endif

# LOCAL
else
    ifneq (,$(wildcard ./.env.example))
        include .env.example
        export
    else
        $(error ".env.example file is missing")
    endif

    ifneq (,$(wildcard ./.env.local))
        include .env.local
        export
    else
        $(error ".env.local file is missing")
    endif
endif

.PHONE: build
build:
	docker compose build --build-arg BUILDKIT_INLINE_CACHE=1

.PHONY: up
up:
	docker compose up -d --build

.PHONY: init
init:
	$(MAKE) online_migrate

.PHONY: down
down:
	docker compose down

.PHONY: restart
restart:
	docker compose restart

.PHONY: destroy
destroy:
	docker compose down --rmi all --volumes --remove-orphans

.PHONY: logs
logs:
	docker compose logs -f

.PHONY: shell
shell:
	docker compose run --rm app bash

.PHONY: online_migrate
online_migrate:
	docker compose run --rm app bash -c "python ./script/database.py --online"

.PHONY: offline_migrate
offline_migrate:
	docker compose run --rm app bash -c "python ./script/database.py"

.PHONY: make_migration
make_migration:
	docker compose run --rm app bash -c "python r./script/un_command.py alembic revision --autogenerate"

.PHONY: flake8
flake8:
	docker compose run --rm app bash -c "python ./script/run_command.py flake8 ./"

.PHONY: mypy
mypy:
	docker compose run --rm app bash -c "python ./script/run_command.py mypy ./"

.PHONY: black
black:
	docker compose run --rm app bash -c "python ./script/run_command.py black ./"

.PHONY: black_check
black_check:
	docker compose run --rm app bash -c "python ./script/run_command.py black ./ --check"

.PHONY: isort
isort:
	docker compose run --rm app bash -c "python ./script/run_command.py isort ./"

.PHONY: isort_check
isort_check:
	docker compose run --rm app bash -c "python ./script/run_command.py isort ./ --check-only"

.PHONY: pytest_html
pytest_html:
	$(MAKE) online_migrate
	docker compose run --rm app bash -c "python ./script/run_command.py pytest -v ./test/ --cov=./src/ --cov-report=html --html=report.html"

.PHONY: pytest_xml
pytest_xml:
	$(MAKE) online_migrate
	docker compose run --rm app bash -c "python ./script/run_command.py pytest -v ./test/ --cov=./src/ --cov-report=xml"

.PHONY: pytest_ci
pytest_ci:
	$(MAKE) up
	$(MAKE) online_migrate
	docker compose run --rm app bash -c "python r./script/un_command.py pytest -v ./test/ --cov=./src/ --junitxml=pytest.xml --cov-report=term-missing:skip-covered | tee pytest-coverage.txt"
