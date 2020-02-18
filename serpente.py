ROMAN_NUMERALS = (
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
)


def encode(n):
    """
    Convert an integer to a string represetation of a roman numeral.
    n: a positive, non-zero integer
    """
    if n <= 0:
        raise ValueError("value must be a non-zero, positive integer")
    encoded = ""
    for symbol, value in ROMAN_NUMERALS:
        while n >= value:
            encoded += symbol
            n -= value
    return encoded


def decode(r):
    """
    Convert a string representation of a roman numeral to an integer.
    r: a string representation of a roman numeral
    """
    decoded, index = 0, 0
    for symbol, value in ROMAN_NUMERALS:
        symlen = len(symbol)
        while r[index : index + symlen] == symbol:
            decoded += value
            index += symlen
    return decoded


__all__ = ["decode", "encode", "ROMAN_NUMERALS"]
