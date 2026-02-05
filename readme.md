# JSON Lexer

Create a basic lexer for a simplified JSON document.

## Learning Outcomes

After completing this experience, learners will be able to:

1. Identify lexical patterns in structured text
2. Implement regular expressions to match language tokens
3. Handle error conditions in lexical analysis

## Usage

You can execute the lexer on example data using:

```sh
python3 lex.py example.json
```

## Testing

The code includes embedded doctests that can be run using:

```sh
make test
```

## Tasks

1. Implement the `lex` function in `lex.py`
2. Ensure all types are correctly identified (boolean, number, string, separator)
3. Report the correct position for each token
4. Raise a `ValueError` for unrecognized input

## Resources

- [Lexical Analysis](https://en.wikipedia.org/wiki/Lexical_analysis) on Wikipedia
- [re](https://docs.python.org/3/library/re.html) module in Python
- [Python generators](https://peps.python.org/pep-0255/) as introduced in PEP 255
