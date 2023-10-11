from math import *
import matplotlib as plt
def task1():
    while True:
        a = float(input('Введите число: '))
        if a<=0:
            print(a,'не является квадратом целого числа')
        elif a**0.5 == int(a**0.5):
            print (a, 'является квадратом целого числа')
        else:
            print (a, 'не является квадратом целого числа')
        if a>1:
            print(a, 'Положительное число')
        elif a == 0:
            print(a, 'не положительное и не отрицательное')
        elif a<1:
            print(a, 'Отрицательное число')


def task2():
    a = float(input('Введите число a: '))
    b = float(input('Введите число b: '))
    x = float(input('Введите число x: '))
    def f(x):
        if x>=0:
            return sin(x)*cos(x) and plt.plot(f(x),sin(x)*cos(x))
        else:
            return sin(x)+cos(x)-1 and plt.plot(f(x),sin(x)*cos(x))
    print(f(x), plt.show())
task2()



