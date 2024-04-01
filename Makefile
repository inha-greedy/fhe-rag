.PHONY: all lint test


# Default target executed when no arguments are given to make.
all: help

test:
	pytest .

######################
# LINTING AND FORMATTING
######################


lint:
	pre-commit run --all-files

######################
# HELP
######################

help:
	@echo '----'
	@echo 'lint                         - run linters'
	@echo 'test                         - run unit tests'
	@echo 'tests                        - run unit tests'
