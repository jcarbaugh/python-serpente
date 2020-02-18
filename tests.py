import unittest

from serpente import encode, decode


class TestCaseConversions(unittest.TestCase):
    def test_decode(self):
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

    def test_encode(self):
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

    def test_random(self):
        """
        Test encoding and decoding of random integers to roman numerals.
        """
        for i in range(1, 3000):
            encoded = encode(i)
            decoded = decode(encoded)
            self.assertEqual(i, decoded)
