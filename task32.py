# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно
# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

from random import randint

num = int(input("Введите количество элементов в списке: "))
list_num = list(randint(1, 100) for _ in range(num))

print(list_num)

limit_min = int(input("Введите минимальное число диапазона: "))
limit_max = int(input("Введите максимальное число диапазона: "))

spisok = list()

def index_num(a, b, c):
    for i in range(len(c)):
        if a < c[i] < b:
            spisok.append(i)
        i += 1
    return spisok

print(index_num(limit_min, limit_max, list_num))