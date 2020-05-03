from quality import arabic_to_roman
import pytest

def test_correct():
    assert arabic_to_roman(1213) == "MCCXIII"
    assert arabic_to_roman(99) == "XCIX"
    assert arabic_to_roman(3000) == "MMM"
    assert arabic_to_roman(100) == "C"

def test_error():
    assert arabic_to_roman(17.3) == "ERROR: It's not an int"
    assert arabic_to_roman(-25.7) == "ERROR: It's not an int"
    assert arabic_to_roman('EC500') == "ERROR: It's not an int"
    assert arabic_to_roman('hello world') == "ERROR: It's not an int"
    assert arabic_to_roman(4999) == "ERROR: It's not in the range(1,4000)"
    assert arabic_to_roman(-5) == "ERROR: It's not in the range(1,4000)"
    assert arabic_to_roman(-1) == "ERROR: It's not in the range(1,4000)"
    assert arabic_to_roman(-8) == "ERROR: It's not in the range(1,4000)"
