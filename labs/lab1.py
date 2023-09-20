#import math as m
from math import *

x = float(input())
y = float(input())
z = float(input())

a = ((x * y)**2 + ((x+y)/2)) / ((x**0.5) - (y**0.5))
b = 2 * sin(x) + ((2*y + log1p(z))**0.5)

print(a,b)
