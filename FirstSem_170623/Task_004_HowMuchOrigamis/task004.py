# Задача 004 Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

total = int(input("Введите общее количество журавликов: "))

peteAndSergTotal = total / 6

kateTotal = peteAndSergTotal * 4

print (f"При условии, что общее количество журавликов {total}, Катя сделала {kateTotal} журавликов, а Петя и Серёжа по {peteAndSergTotal} журавликов.")