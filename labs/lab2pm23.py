from math import *
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
def decimnal_in_new_numeal_system(number,base):
    t = 1
    d = 0
    while number > 0:
         d = d + (number % base) * t
         t = t * 10
         number = number // base
    return d
def task3():
    osn = int(input('Введите систему счисления: ' ))
    print(decimnal_in_new_numeal_system(float(input('Введите число в десятичной С.С.: ')),osn))
def task5():
    a = str(input('Введите первое число: '))[-1:]
    b = str(input('Введите второе число: '))[-1:]
    c = str(input('Введите третье число: '))[-1:]
    d= int(a) + int(b) + int(c)
    if d % 2 == 0:
        print('Сумма последних цифр заданных чисел чётная')
        if int(str(d)[-1:])%2 == 0:
            print("Последняя цифра суммы чётная")
        else:
            print("Последняя цифра суммы нечётная")
    else:
        print('Сумма последних цифр заданных чисел нечётная')
def task6():
    labs = int(input('Введите количество несданных лабораторных работ: '))
    consultations_per_month = int(input('Введите количество посещённых консультаций в месяц: '))
    attemps = int(input('Введите количество попыток до сдачи лабораторной работы: '))




