# coding=utf-8
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    row = [1, 1]
    if m <= 2:
        return row
    else:
        for itm in range(2, m + 1):
            row.append(row[itm - 2] + row[itm - 1])
        return row[n:m]


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range (len(origin_list)-1):
        for jtm in range (len(origin_list)- i - 1):
            if origin_list[jtm] > origin_list[jtm + 1]:
                origin_list[jtm], origin_list[jtm + 1] = origin_list[jtm + 1], origin_list[jtm]
    return origin_list


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def great_null(fun, my_list1):
    apl = []
    for x in my_list1:
        if fun(my_list1[x]) == True:
            apl.append(my_list1[x])
    return apl

def fun (elem):
    if elem > 0:
        return True

my_list = [5, -4, -25, 48, -8, 100, 67]


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

import math

def vertex_traillogram(A1, A2, A3, A4):

    len_A1A2 = math.sqrt(( A2[0] - A1[0] ) ** 2 + ( A2[1] - A1[1] ) ** 2 )
    len_A4A3 = math.sqrt(( A3[0] - A4[0] ) ** 2 + ( A3[1] - A4[1] ) ** 2 )
    len_A1A4 = math.sqrt(( A4[0] - A1[0] ) ** 2 + ( A4[1] - A1[1] ) ** 2 )
    len_A2A3 = math.sqrt(( A3[0] - A2[0] ) ** 2 + ( A3[1] - A2[1] ) ** 2 )
    if (len_A1A2 == len_A4A3) & (len_A1A4 == len_A2A3):
          return True
    else:
          return False

print(vertex_traillogram((1, 3), (4, 7), (2, 8), (-1, 4)))