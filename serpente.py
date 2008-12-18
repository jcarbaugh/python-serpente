
__version__ = "0.1"
__license__ = "BSD License"
__author__ = "Jeremy Carbaugh <jeremy@200ok.net>"

import random
import unittest

ROMAN_NUMERALS = (
    (u"M", 1000),
    (u"CM", 900),
    (u"D", 500),
    (u"CD", 400),
    (u"C", 100),
    (u"XC", 90),
    (u"L", 50),
    (u"XL", 40),
    (u"X", 10),
    (u"IX", 9),
    (u"V", 5),
    (u"IV", 4),
    (u"I", 1),
)

def encode(n):
    """
    Convert an integer to a string represetation of a roman numeral.
    n: a positive, non-zero integer
    """
    if n <= 0:
        raise ValueError, "value must be a non-zero, positive integer"
    encoded = u""
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
        self.assertEqual(decode(u"I"), 1)
        self.assertEqual(decode(u"II"), 2)
        self.assertEqual(decode(u"IV"), 4)
        self.assertEqual(decode(u"V"), 5)
        self.assertEqual(decode(u"VI"), 6)
        self.assertEqual(decode(u"VIII"), 8)
        self.assertEqual(decode(u"IX"), 9)
        self.assertEqual(decode(u"X"), 10)
        self.assertEqual(decode(u"XI"), 11)
        self.assertEqual(decode(u"XXXII"), 32)
        self.assertEqual(decode(u"XLV"), 45)
        
    def testencode(self):
        """
        Test encoding of integers of roman numerals.
        """
        self.assertEqual(encode(1), u"I")
        self.assertEqual(encode(2), u"II")
        self.assertEqual(encode(4), u"IV")
        self.assertEqual(encode(5), u"V")
        self.assertEqual(encode(6), u"VI")
        self.assertEqual(encode(8), u"VIII")
        self.assertEqual(encode(9), u"IX")
        self.assertEqual(encode(10), u"X")
        self.assertEqual(encode(11), u"XI")
        self.assertEqual(encode(32), u"XXXII")
        self.assertEqual(encode(45), u"XLV")
        
    def testrandom(self):
        """
        Test encoding and decoding of random integers to roman numerals.
        """
        for i in range(1, 10000):
            x = random.randint(1, 3000)
            encoded = encode(x)
            decoded = decode(encoded)
            self.assertEqual(x, decoded)
    
if __name__ == "__main__":
    unittest.main()
    
__all__ = ['decode','encode','ROMAN_NUMERALS']