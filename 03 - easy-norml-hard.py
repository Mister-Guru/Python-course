#Easy
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("Easy. Задача 1")
def my_round(number, ndigits):
    number *= 10**5
    if number % 1 >=0.5 :
        number = number // 1 + 1
    else :
        number //= 1
        
    string = str(number / 10**5)
    return '{:.7}'.format(string) # Так и не разобрался с форматом, чтобы вместо 2.2 выводилось 2.20000

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5)) 
print(my_round(2.9999967, 5))
print('')


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("Easy. Задача 2")
"""
Возможно есть более лаконичное решение этой задачи
"""
def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    sr = str(ticket_number)
    if len(sr) == 6 : 
        sr1 = sr[:3]
        sr2 = sr[3:]
        for i in sr1 :
            sum1 += int(i)
        for j in sr2 :
            sum2 += int(j)
        if sum1 == sum2 :
            return "Congrats! Lucky Ticket!"
        else :
            return "Sorry. Unlucky Ticket :("
    else :
        return "Incorrect number" #если в билете меньше 6-ти цифр выводим просто его номер 
    
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print('')
# Normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Normal. Задача 1")
def fibonacci(n, m):
    fib_seq = [1, 1]
    for i in range(2, m+1) :
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq[n-1:m]

print(fibonacci(3,7))
print('')
# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
import random
print("Normal. Задача 2")
def sort_to_max(origin_list):
    n = len(origin_list)
    tmp = 0.1
    for i in range(0,n-1) :
        for j in range(i+1,n-1) :
            if origin_list[j] <= origin_list[i] :
                tmp = origin_list[j]
                origin_list[j] = origin_list[i]
                origin_list[i] = tmp
    print(origin_list)
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
# Не понимаю почему не сортирует '0', на выходе ставит его самим большим элементом
print('')
# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
"""
Пытался сделать с лямбдой и map , сделал так
"""
print("Normal. Задача 3")
def my_filter(cond, lst):
    new_list = list()
    for x in lst:
        if x >= cond :
            new_list.append(x)
        else:
            continue
    return new_list      
print(my_filter(5,[1,2,3,4,5,6,7,8,9,10]))
print('')
# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
'''
Алгоритм такой - вычисляю длины сторон и сравниваю противополжные
стороны. Если они равны - значит параллелограмм.
'''
def isParallelogramm(A,B,C,D):
    ax = float(A[0])
    ay = float(A[1])
    bx = float(B[0])
    by = float(B[1])
    cx = float(C[0])
    cy = float(C[1])
    dx = float(D[0])
    dy = float(D[1])
    ab = ((by-ay)**2+(bx-ax)**2)**0.5
    bc = ((cy-by)**2+(cx-bx)**2)**0.5
    cd = ((dy-cy)**2+(dx-cx)**2)**0.5
    da = ((dy-ay)**2+(dx-ax)**2)**0.5
    if (ab == cd) & (bc == da) :
        return "{!s}".format("It is parallelogram")
print(isParallelogramm([0,0],[1,1],[4,1],[3,0]))
print('')    
