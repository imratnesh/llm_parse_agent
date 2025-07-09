import pytest
from main import add

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-2, -3) == -5

def test_add_zero():
    assert add(0, 0) == 0

def test_add_mixed():
    assert add(-2, 3) == 1
