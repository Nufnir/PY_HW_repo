# Задача 008. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

print(f"Введите размер шоколадки:")

sideN = int(input("Одна сторона шоколадки > "))

sideM = int(input("Вторая сторона шоколадки > "))

bitK = int(input("Введите количество долек, предполагающихся к отделению от куска: "))

n = sideN

m = sideM

if sideM * sideN == bitK:
    print("Площадь шоколадки равна куску, который вы хотите отломить.")
    exit()
else:
    while m > 1:
        if sideN * (m - 1) == bitK:
            print(f"От шоколадки размером {sideN} на {sideM} долек можно отломить кусок размером {bitK} долек.")
            exit()
        else:
            m -= 1
    
    while n > 1:
        if sideM * (n - 1) == bitK:
            print(f"От шоколадки размером {sideN} на {sideM} долек можно отломить кусок размером {bitK} долек.")
            exit()
        else:
            n -= 1
print(f"От шоколадки размером {sideN} на {sideM} долек нельзя отломить кусок размером {bitK} долек.")