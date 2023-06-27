# Задача 012. Задумано два натуральных числа X и Y (X,Y≤1000), нужно их отгадать.
#Есть две подсказки. Сумма этих чисел S и их произведение P.

print("Загадайте два числа.")
number_sum = int(input("Введите сумму этих чисел: "))
number_mult = int(input("Введите произведение этих чисел: "))
for i in range(number_sum):
    for j in range(number_mult):
        if number_sum == i + j and number_mult == i * j:
            print(f"Загаданы числа {i} и {j}")