bundle:
	shiv -c gallery -o ~/bin/gallery .

viewer:
		shiv -c viewer -o ~/bin/gallery-viewer .

.PHONY: test
test:
	pytest test/unit

.PHONY: integration-test
integration-test:
	pytest test/integration

.PHONY: test-all
test-all:
	pytest

venv:
	python -m venv .venv

dev-environment:
	pip install ".[test]"

build:
	fpm -s python -t deb .
