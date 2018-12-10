SHELL := /bin/bash
.DEFAULT_GOAL := help

DAY := 3

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install-dependencies
install-dependencies:  ## install python dependencies
	pip install -r requirements.txt

.PHONY: clean
clean:  ## cleans the project locally
	python3 setup,py clean

.PHONY: build
build:  ## builds the project locally
	python3 setup.py build

.PHONY: run
run:  ## run the day set in main.py
	python3 src/__init__.py $(DAY)

.PHONY: check
check:  ## run linter
	pycodestyle .

.PHONY: test
test:  ## run the tests
	python3 setup.py pytest

.PHONY: install
install: build  test ## install the lib
	python3 setup.py install

.PHONY: package
package: build test ## build package
	python3 setup.py sdist
