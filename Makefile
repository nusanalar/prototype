# Nusa Nalar prototype.
.DEFAULT_GOAL := help
PYTHON ?= python3
NODE ?= node
PORT ?= 8000
ASSETS ?= ../assets
SCRIPTS ?= ../scripts
ARGS ?=
TESTS := $(sort $(wildcard tests/t*.js))

.PHONY: help serve test voxsync voices

help:
	@echo 'make serve      Play it at http://127.0.0.1:$(PORT)/ (PORT=8000)'
	@echo 'make test       Run every Playwright test in tests/ (or one: make test TESTS=tests/t17.js)'
	@echo 'make voxsync    Embed the recorded voice lines from $(ASSETS) (id and en) into index.html'
	@echo 'make voices     Generate missing voice lines into $(ASSETS), then embed them (ARGS="--lang en")'

serve:
	$(PYTHON) -m http.server $(PORT) --bind 127.0.0.1

test:
	@set -e; for t in $(TESTS); do echo "== $$t"; $(NODE) $$t; done

voxsync:
	$(PYTHON) tools/voxsync.py $(ASSETS)

voices:
	$(MAKE) -C $(SCRIPTS)/voice-generator sync ASSETS=$(abspath $(ASSETS)) ARGS='$(ARGS)'
	$(MAKE) voxsync
