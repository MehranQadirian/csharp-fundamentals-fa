# Build the PDF locally:  make pdf        (version label: make pdf VERSION=1.0.0)
VERSION ?= dev

.PHONY: setup pdf clean

setup:
	pip install -r requirements.txt
	playwright install chromium

pdf:
	cd book && BOOK_VERSION=$(VERSION) python3 make_covers.py && BOOK_VERSION=$(VERSION) python3 build.py
	@echo "-> book/dist/C-Sharp-Fundamentals.pdf"

clean:
	rm -rf book/dist book/body.* book/cover.* book/back.* book/final.pdf
