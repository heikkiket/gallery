#: Print out this help message
help:
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
		| grep -v -- -- \
		| sed 'N;s/\n/###/' \
		| sed -n 's/^#: \(.*\)###\(.*\):.*/\2###\1/p' \
		| column -t  -s '###'

build-all: bundle viewer deb

#: Create a Python bundle from photos and photo-viewer with shiv
bundle:
	@mkdir -p	bin
	shiv -c photos -o ./bin/photos .
	shiv -c photo-viewer -o ./bin/photo-viewer .

#: Create a deb package
deb:
	@mkdir -p	bin
	fpm -s python -t deb -p bin .

.PHONY: test
#: Run unit tests
test:
	.venv/bin/pytest test/unit

.PHONY: integration-test
#: Run integration tests
integration-test:
	.venv/bin/pytest test/integration

.PHONY: test-all
#: Run all tests
test-all:
	.venv/bin/pytest

#: Create venv for project
venv:
	python -m venv .venv

#: Install dev dependencies
dev-environment:
	pip install ".[test]"

#: Clean build artifacts
clean:
	rm -R bin
	rm -R build
