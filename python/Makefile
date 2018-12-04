SHELL := /bin/bash
.DEFAULT_GOAL := help

DAY := 02

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: install-dependencies
install-dependencies:  ## install python dependencies
	pip install -r requirements.txt

.PHONY: run
run:
	python src/day_$(DAY).py

.PHONY: check
check:  ## run linter
	pycodestyle .

.PHONY: test
test:  ## run the tests
	py.test --cov
