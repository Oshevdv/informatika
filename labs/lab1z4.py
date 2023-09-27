from math import *
# # Задание №1
def task1():
 x = float(input("Введите X: "))
 y = float(input("Введите Y: "))
 z = float(input("Введите Z: "))

 a = ((x * y)**2 + ((x+y)/2)) / ((x**0.5) - (y**0.5))
 b = 2 * sin(x) + ((2*y + log1p(z))**0.5)

 print(a,b)

# # Задание №2
def task2():
    a = -3
    b = -1
    c = 0.2
    def f(x):
        x = ((a * x**2 + b) / (x**4)**(1/3)) * c + x**a
        return x
    print(f(float(input("Введите X: "))))

# # Задание №3
def task3():
    def f(x):
        x = (abs(log(cosh(x**3),3)))/(sinh((x**3) + x**(1/3)))
        return x
    print(f(float(input("Введите Х: "))))

# # Задание №4
def task4():
        st_osn = float(input("Введите сторону основания: "))
        s_bok = float(input("Введите площадь боковой грани: "))
        st_bok = s_bok / st_osn
        diag_prizm = sqrt(st_osn**2 + st_bok**2)
        r_prizm = diag_prizm/2
        print(r_prizm)

# # Задание №5
def task5():
    mass_1 = float(input("Введите массу первой тележки: "))
    speed_1 = float(input("Введите скорость первой тележки: "))
    mass_2 = float(input("Введите массу второй тележки: "))
    speed_2 = float(input("Введите скорость второй тележки: "))
    speed_all = 0
    if mass_1 * speed_1 > mass_2 * speed_2:
        speed_all = (mass_1 * speed_1 - mass_2 * speed_2) / (mass_1 + mass_2)
        print("Тележки движутся в направлении первой тележки со скоростью", speed_all)
    else:
        speed_all = (mass_2 * speed_2 - mass_1 * speed_1) / (mass_2 + mass_1)
        print("Тележки движутся в направлении второй тележки со скоростью", speed_all)
def task6():
    s_pov_kub = float(input())
    x = sqrt(s_pov_kub/6*pi)
    s_shar = pi ** x



