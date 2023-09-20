import math as m
def f(x):
    x = (abs(m.log(m.cosh(x**3),3)))/(m.sinh((x**3) + x**(1/3)))
    return x
print(f(5))
