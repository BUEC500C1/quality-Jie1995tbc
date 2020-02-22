from quality import arabic_to_roman
import pytest

def test_correct():
    assert arabic_to_roman(1213) == "MCCXIII"
    assert arabic_to_roman(99) == "XCIX"
    assert arabic_to_roman(3000) == "MMM"
    assert arabic_to_roman(100) == "C"

def test_error():
    assert arabic_to_roman(4999) == "ERROR: OVERFLOW"
    assert arabic_to_roman(6000) == "ERROR: OVERFLOW"
    assert arabic_to_roman(-5) == "ERROR: OVERFLOW"
    assert arabic_to_roman(-1) == "ERROR: OVERFLOW"
    assert arabic_to_roman(-8) == "ERROR: OVERFLOW"