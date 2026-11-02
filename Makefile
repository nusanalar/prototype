# Nusa Nalar prototype.
.DEFAULT_GOAL := help
PYTHON ?= python3
NODE ?= node
PORT ?= 8000
ASSETS ?= ../assets
TESTS := $(sort $(wildcard tests/t*.js))

.PHONY: help serve test voxsync voxscript

help:
	@echo 'make serve      Play it at http://127.0.0.1:$(PORT)/ (PORT=8000)'
	@echo 'make test       Run every Playwright test in tests/ (or one: make test TESTS=tests/t17.js)'
	@echo 'make voxsync    Copy the voice MP3s from the asset kit $(ASSETS) (id and en) into voices/ and link them in index.html'
	@echo '                (voices are generated in the assets repo: make voices there)'
	@echo 'make voxscript  Add a voice line for every text in the page to $(ASSETS)/voices/*/lines.json and write voices/SCRIPT.md'

serve:
	$(PYTHON) -m http.server $(PORT) --bind 127.0.0.1

test:
	@set -e; for t in $(TESTS); do echo "== $$t"; $(NODE) $$t; done

voxsync:
	$(PYTHON) tools/voxsync.py $(ASSETS)

voxscript:
	$(NODE) tools/voxscript.js $(ASSETS)
