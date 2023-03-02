"""
Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий по величине элемент к заданному числу X.
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
N = int(input("Введите количество элементов массива  "))
import random
list=[]
for i in range(N):
    list.append(random.randint(1,100))

X = int(input("Введите число "))
print(list)

count = 1
"""
for i in range(N):
    if X == list[i]:
        print(list[i]) 
        break
    elif X - count == list[i]:
        print(list[i])
        break
    elif X + count == list[i]:
        print(list[i])
        break
    else: count +=1
def fun(Array,X,count):
    for i in range(N):
    if X == list[i] or X - count == list[i] or X + count == list[i] :
        print(list[i]) 
        break
 
"""
break_out_flag = False
for count in range(N):
    for i in range(N):
        if X == list[i] or X - count == list[i] or X + count == list[i] :
            print(list[i]) 
            break_out_flag = True
            break 
    if break_out_flag:
        break