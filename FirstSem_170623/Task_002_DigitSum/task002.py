# Задача 002 найти сумму цифр трёхзначного числа

numberA = input("Введите трёхзначное число: ")

digitA, digitB, digitC = [int(i) for i in str(numberA)]

sum = digitA + digitB + digitC

print(f"Сумма цифр числа {numberA} равна {sum}.")