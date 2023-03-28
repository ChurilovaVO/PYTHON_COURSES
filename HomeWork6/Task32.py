# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
import random
values=tuple(map(int, input('Введите min и max значения через пробел: ').split()))
list=[random.randint(0,30) for i in range(10)]
print(list)
index=0
result_list=[]
for i in list:
    if values[0]<i<values[1]:
        result_list.append(index)
    index+=1
print(result_list)
