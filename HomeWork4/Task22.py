# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
size1=int(input('Введите размер первого множества: '))
size2=int(input('Введите размер второго множества: '))
list1=[random.randint(1,10) for i in range(size1)]
list2=[random.randint(1,10) for i in range(size2)]
print(list1)
print(list2)
result_list=[]
for i in list1:
    for j in list2:
        if i==j:
            result_list.append(j)
result_list=set(result_list)
result_list=list(result_list)

min=result_list[0]
for i in result_list[1:]:
    if i<min:
        min=i
print(result_list)

