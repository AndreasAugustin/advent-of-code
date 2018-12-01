SHELL := /bin/bash
.DEFAULT_GOAL := help

.PHONY: help
help:  ## help target to show available commands with information
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |  awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: docker-build
docker-build: ## Build Container
	docker-compose build

.PHONY: shell
shell: docker-build ## Build container
	docker-compose run py sh

.PHONY: tmux
tmux: docker-build ## Build container
	docker-compose run py tmux
