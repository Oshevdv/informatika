from math import *
a = -3
b = -1
c = 0.2
def f(x):
    x = ((a * x**2 + b) / (x**4)**(1/3)) * c + x**a
    return x
print(f(5))
