all: test

test:
	python3 -m doctest lex.py

clean:
	rm -f jsonlex
