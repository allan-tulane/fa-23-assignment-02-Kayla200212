from main.py import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(2)) == 4*2
    assert subquadratic_multiply(BinaryNumber(1), BinaryNumber(7)) == 1*7
