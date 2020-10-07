import pytest
from calculator import add

def tests_add_floats():
    assert add(2.0,4.5) == 6.5

def tests_add_str():
    assert add('2') == 2
    

def tests_add_integer():
    assert add(2,4,1,4) == 11
    assert add(2,4) == 6
