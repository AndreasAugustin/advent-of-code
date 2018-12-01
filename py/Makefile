SHELL := /bin/bash
.DEFAULT_GOAL := help

PROJECT := 01

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install-dependencies
install-dependencies:  ## install python dependencies
	pip install -r requirements.txt

.PHONY: check
check:  ## run linter
	pylint src/ test/

.PHONY: test
test:  ## run the tests
	python $(PROJECT)/main_test.py
