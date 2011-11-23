__version__ = "1.0.0"
__license__ = "BSD License"
__author__ = "Jeremy Carbaugh <jeremy@200ok.net>"

import unittest

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
        while r[index:index+symlen] == symbol:
            decoded += value
            index += symlen
    return decoded
    
class TestCaseConversions(unittest.TestCase):

    def testdecode(self):
        """
        Test decoding of roman numerals to integers.
        """
        self.assertEqual(decode("I"), 1)
        self.assertEqual(decode("II"), 2)
        self.assertEqual(decode("IV"), 4)
        self.assertEqual(decode("V"), 5)
        self.assertEqual(decode("VI"), 6)
        self.assertEqual(decode("VIII"), 8)
        self.assertEqual(decode("IX"), 9)
        self.assertEqual(decode("X"), 10)
        self.assertEqual(decode("XI"), 11)
        self.assertEqual(decode("XXXII"), 32)
        self.assertEqual(decode("XLV"), 45)
        
    def testencode(self):
        """
        Test encoding of integers of roman numerals.
        """
        self.assertEqual(encode(1), "I")
        self.assertEqual(encode(2), "II")
        self.assertEqual(encode(4), "IV")
        self.assertEqual(encode(5), "V")
        self.assertEqual(encode(6), "VI")
        self.assertEqual(encode(8), "VIII")
        self.assertEqual(encode(9), "IX")
        self.assertEqual(encode(10), "X")
        self.assertEqual(encode(11), "XI")
        self.assertEqual(encode(32), "XXXII")
        self.assertEqual(encode(45), "XLV")
        
    def testrandom(self):
        """
        Test encoding and decoding of random integers to roman numerals.
        """
        for i in range(1, 3000):
            encoded = encode(i)
            decoded = decode(encoded)
            self.assertEqual(i, decoded)
    
if __name__ == "__main__":
    unittest.main()
    
__all__ = ['decode','encode','ROMAN_NUMERALS']