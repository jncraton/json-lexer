all: test

test:
	python3 -m doctest lex.py

run:
	python3 lex.py example.json

format:
	uvx black==26.1.0 lex.py

clean:
	rm -rf jsonlex __pycache__
