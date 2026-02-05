JSON Lexer
----------

A class assignment to create a basic lexer for a JSON document.

Assignment
----------

Edit the function `lex` in lex.py to make all included doctests pass.

Testing
-------

You can run the tests by calling:

```sh
python3 -m doctest lex.py
```

or

```sh
make test
```

## Tasks

1. Implement the `lex` function in `lex.py`
2. Ensure all types are correctly identified (boolean, number, string, separator)
3. Report the correct position for each token
4. Raise a `ValueError` for unrecognized input

## Resources

- [WP: Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis)
- [re](https://docs.python.org/3/library/re.html) module in Python
