.PHONY: check pdf all clean

PYTHON ?= python3

all: check pdf

check:
	$(PYTHON) scripts/check_identities.py
	$(PYTHON) scripts/check_streamlined.py

pdf:
	$(PYTHON) scripts/build_pdfs.py

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('build', ignore_errors=True)"

