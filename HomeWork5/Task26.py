# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

num1=int(input('Введите первое число: '))
num2=int(input('Введите второе число: '))

def degree (A,B)-> int:
    if B==1:
        return A
    return degree(A,B-1)*A

print(degree(num1,num2))
    
