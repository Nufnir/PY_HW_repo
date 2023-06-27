# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].

import random
random_list = []
top_limit = int(input("Введите максимальную длину массива чисел: "))
x_number = int(input("Введите число, которое нужно найти: "))
total_count = 0

for i in range(0,top_limit):
    n = random.randint(1,100)
    random_list.append(n)

for j in random_list:
    if j == x_number:
        total_count += 1

print(random_list)

if total_count == 0:
    print(f"Число {x_number} в массиве чисел не встречается.")
else:
    print(f"Число {x_number} в массиве чисел встречается {total_count} раз.")