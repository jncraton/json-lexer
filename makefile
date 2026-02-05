all: test

test:
	python3 -m doctest lex.py

run:
	python3 lex.py example.json

clean:
	rm -rf jsonlex __pycache__
