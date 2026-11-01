# Nusa Nalar prototype.
.DEFAULT_GOAL := help
PYTHON ?= python3
NODE ?= node
PORT ?= 8000
ASSETS ?= ../assets
TESTS := $(sort $(wildcard tests/t*.js))

.PHONY: help serve test voxsync

help:
	@echo 'make serve      Play it at http://127.0.0.1:$(PORT)/ (PORT=8000)'
	@echo 'make test       Run every Playwright test in tests/ (or one: make test TESTS=tests/t17.js)'
	@echo 'make voxsync    Copy the voice lines from the asset kit $(ASSETS) (id and en) into index.html'
	@echo '                (voices are generated in the assets repo: make voices there)'

serve:
	$(PYTHON) -m http.server $(PORT) --bind 127.0.0.1

test:
	@set -e; for t in $(TESTS); do echo "== $$t"; $(NODE) $$t; done

voxsync:
	$(PYTHON) tools/voxsync.py $(ASSETS)
