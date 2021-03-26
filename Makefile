PYTHON       = $(shell which python)
SHELL_FILES  = $(shell find . -maxdepth 1 -type f -name \*.sh)
PYTHON_FILES = $(shell find . -maxdepth 1 -type f -name \*.py)
APPLICATION  = $(shell find . -maxdepth 1 -type f -name \*.py | sort | grep -v config)

all:
	$(PYTHON) ./analyze-candidate.py

lint:
	flake8 --statistics $(PYTHON_FILES)

requirements:
	$(PYTHON) -m pip install -U -r requirements.txt
