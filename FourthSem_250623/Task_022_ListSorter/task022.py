# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

list_a = []
list_b = []
top_limit_a = int(input("Введите максимальную длину массива чисел A: "))
top_limit_b = int(input("Введите максимальную длину массива чисел B: "))

def fill_list(top_limit):
    new_list = []
    for i in range(0,top_limit):
        n = int(input("Введите очередное число массива чисел: "))
        new_list.append(n)
    return new_list

print("Заполняем массив чисел А:")
list_a = fill_list(top_limit_a)
print("Заполняем массив чисел B:")
list_b = fill_list(top_limit_b)
sorted_list_a = sorted(set(list_a))
sorted_list_b = sorted(set(list_b))
print(f"Вывод отсортированного массива чисел А без повторений: {sorted_list_a}")
print(f"Вывод отсортированного массива чисел B без повторений: {sorted_list_b}")