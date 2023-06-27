# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.

import random
random_list = []
top_limit = int(input("Введите максимальную длину массива чисел: "))
x_number = int(input("Введите число, близкое к которому нужно найти: "))
total_count = 0

for i in range(0,top_limit):
    n = random.randint(1,100)
    random_list.append(n)

def nearest_value(random_list, x_number):
    found = random_list[0]
    for item in random_list:
        if abs(item - x_number) < abs(found - x_number):
            found = item
    return found
 
print(f"Ближайшее число к {x_number} в массиве чисел {random_list} является {nearest_value(random_list, x_number)}")