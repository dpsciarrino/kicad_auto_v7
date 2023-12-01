PYTHON = python3

.PHONY = config project

config:
	$(PYTHON) kicad7_proj.py config

project:
	$(PYTHON) kicad7_proj.py build