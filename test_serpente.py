from serpente import encode, decode


def test_decode():
    """
    Test decoding of roman numerals to integers.
    """
    assert decode("I") == 1
    assert decode("II") == 2
    assert decode("IV") == 4
    assert decode("V") == 5
    assert decode("VI") == 6
    assert decode("VIII") == 8
    assert decode("IX") == 9
    assert decode("X") == 10
    assert decode("XI") == 11
    assert decode("XXXII") == 32
    assert decode("XLV") == 45


def test_encode():
    """
    Test encoding of integers of roman numerals.
    """
    assert encode(1) == "I"
    assert encode(2) == "II"
    assert encode(4) == "IV"
    assert encode(5) == "V"
    assert encode(6) == "VI"
    assert encode(8) == "VIII"
    assert encode(9) == "IX"
    assert encode(10) == "X"
    assert encode(11) == "XI"
    assert encode(32) == "XXXII"
    assert encode(45) == "XLV"


def test_random():
    """
    Test encoding and decoding of integers from 1 to 3000.
    """
    for i in range(1, 3000):
        encoded = encode(i)
        decoded = decode(encoded)
        assert i == decoded
