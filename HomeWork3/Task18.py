# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
size=int(input('Введите размер массива: '))
list=[random.randint(1,20) for i in range(size)]
print(*list)

number=int(input('Введите число: '))
diff_list=[]
index=0
for i in list:
    diff_list.append(i-number)
    if diff_list[index]<0:
        diff_list[index]=-diff_list[index]
    index+=1
#print(diff_list)

min=diff_list[0]
for i in diff_list:
    if i<min:
        min=i
#print(min)
index2=0
for i in diff_list:
    if i!=min:
        index2+=1
    else:   
        #print(index2)
        print(list[index2])
        break