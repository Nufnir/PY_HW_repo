# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

number_a = int(input("Введите число: "))
degree_num = int(input("Введите степень числа: "))

def func(a, b):
    if b == 0:
        return 1
    return a * func(a, b - 1)

print(f"Число {number_a} в степени {degree_num} равно {func(number_a, degree_num)}")