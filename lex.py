import re
import sys
import enum


def lex(src):
    """
    Returns a generator of (name, value, position) tuples for a simplified
    JSON document.

    Examples:

    >>> next(lex('true'))
    ('boolean', 'true', 0)

    >>> next(lex('false'))
    ('boolean', 'false', 0)

    >>> next(lex('5'))
    ('number', '5', 0)

    >>> next(lex('3.14'))
    ('number', '3.14', 0)

    >>> next(lex('-1.61'))
    ('number', '-1.61', 0)

    >>> next(lex('"Hello"'))
    ('string', 'Hello', 0)

    >>> next(lex('{'))
    ('separator', '{', 0)

    >>> list(lex('[1, "2"]'))
    [('separator', '[', 0), ('number', '1', 1), ('separator', ',', 2), ('string', '2', 4), ('separator', ']', 7)]

    >>> list(lex('{"a": 1}'))
    [('separator', '{', 0), ('string', 'a', 1), ('separator', ':', 4), ('number', '1', 6), ('separator', '}', 7)]

    >>> list(lex('[1, --2]'))
    Traceback (most recent call last):
    ...
    ValueError: Unrecognized token starting at position 4
    """


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        [print(t) for t in lex(f.read())]
