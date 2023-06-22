# Задача 006. Посчитать счастливый ли билет.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.

ticketNumber = input("Введите шестизначный номер билета: ")

digitA, digitB, digitC, digitD, digitE, digitF = [int(i) for i in str(ticketNumber)]

sumFirst = digitA + digitB + digitC

sumLast = digitD + digitE + digitF


if sumFirst == sumLast:
    print(f"Этот билет счастливый!\nCумма {digitA} {digitB} и {digitC} равна сумме {digitD} {digitE} и {digitF}! :)")
else:
    print(f"Этот билет не счастливый.\nCумма {digitA} {digitB} и {digitC} не равна сумме {digitD} {digitE} и {digitF}. :(")