"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y



def subquadratic_multiply(x, y):
    ### TODO
  #almost the same as the _quadratic_multiply from lab 3
    yvec = y.binary_vec
    xvec = x.binary_vec

    xvec, yvec = pad(xvec, yvec)

    if x.decimal_val <= 1 and y.decimal_val <=1: #base case is if both are <=1
      return BinaryNumber(x.decimal_val * y.decimal_val)#then return their prod

    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)#split both into halves
    
    prod1 = subquadratic_multiply(x_left, y_left)
    prod2 = subquadratic_multiply(x_left, y_right)
    prod3 = subquadratic_multiply(x_right, y_left)
    prod4 = subquadratic_multiply(x_right, y_right)
    #Use `bit_shift` to do the 2^n and 2^{n/2} multiplications.
    exp = bit_shift(BinaryNumber(2), len(xvec)).decimal_val#2^n
    exp2 = bit_shift(BinaryNumber(2), len(xvec)//2).decimal_val#2^n/2
    #combine it all
    return exp*prod1 + exp2*(prod2+prod3)+prod4
    ###



def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000

    
    

