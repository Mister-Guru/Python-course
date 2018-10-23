__author__ = 'Пастушенко Андрей Анатольевич'

#Easy

print('''Задание-1:
         Дан список, заполненный произвольными целыми числами. 
         Получить новый список, элементы которого будут
         квадратами элементов исходного списка
         [1, 2, 4, 0] --> [1, 4, 16, 0]
      ''')

lst1 = [1, 2, 4, 0]
lst2 = [el**2 for el in lst1[:]]
print("Исходный список - ", lst1)
print("Полученный список - ", lst2)

print('''Задание-2:
         Даны два списка фруктов.
         Получить список фруктов, присутствующих в обоих исходных списках.

      ''')
fruit1 = ['Яблоко','Киви','Банан','Ананас','Апельсин','Манго','Мандарин']
fruit2 = ['Яблоко','Банан','Апельсин','Мандарин']
fruit3 = [fr for fr in fruit1 if fr in fruit2 ]

''' Можно ещё так:
for item in lst1 :
    if item in lst2 :
        lst3.append(item)
'''
print(fruit3)

print('''Задание-3:
         Дан список, заполненный произвольными числами.
         Получить список из элементов исходного, удовлетворяющих следующим условиям:
         + Элемент кратен 3
         + Элемент положительный
         + Элемент не кратен 4

      ''')         
import random
lst = [i for i in random.sample(range(-100,100),100) if (i>0) & (not i%3) & (i%4) ]
print("Список чисел, удовлетворяющих критерию - ", lst)

#Normal

import re
import random


print('''Задание-1: ')
         Вывести символы в нижнем регистре, которые находятся вокруг
         1 или более символов в верхнем регистре.
         Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
         Решить задачу двумя способами: с помощью re и без.

      ''') 
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'

# Вариант с re
res_re1 = [i for i in re.findall('([a-z]+)[A-Z]', line)]
print(res_re1)

# Вариант без re
res1 = list()
found1 = ''
for i in range(len(line)) :
    if line[i].islower() :
        found1 += line[i]
    else:
        if line[i - 1].islower():
            res1.append(found1)
            found1 = ''
print(res1)


print('Задание-2:')
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.

line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'

# Вариант 1 с помощью re
res_re2 = [x for x in re.findall('[a-z][a-z]([A-Z]+)[A-Z][A-Z]', line_2)]
print(res_re2)

# Вариант 2
res2 = list()
found2 = ''

for i in range(len(line_2)):
    try:
        if (line_2[i - 2].islower() and line_2[i - 1].islower() and line_2[i].isupper()) or len(
                found2) > 0:
            found2 += line_2[i]
            if line_2[i + 1].isupper() and line_2[i + 2].isupper():
                if line_2[i + 2].isupper() and line_2[i + 3].isupper():
                    pass
                else:
                    res2.append(found2)
                    found2 = ''

            else:
                found2 = ''

    except IndexError:
        pass

print (res2)

print('''Задание-3:
         Напишите скрипт, заполняющий указанный файл (самостоятельно задайте имя файла)
         произвольными целыми цифрами, в результате в файле должно быть
         2500-значное произвольное число.
         Найдите и выведите самую длинную последовательность одинаковых цифр
         в вышезаполненном файле.

      ''')
f = open('newfile.txt', 'w', encoding='utf-8')
n = [str(random.randint(0, 9)) for _ in range(2499)]
n = str(random.randint(0, 9)) + ''.join(n)
f.write(n)

f = open('newfile.txt', 'r', encoding='utf-8')
num = f.readline()
ptrn = '([0]{2,}|[1]{2,}|[2]{2,}|[3]{2,}|[4]{2,}|' \
           '[5]{2,}|[6]{2,}|[7]{2,}|[8]{2,}|[9]{2,})'
seq = re.findall(ptrn, num)
print(seq)
long_seq = []
[long_seq.insert(0, x) for x in seq if len(x) > len(long_seq)]
print(long_seq[0])

#Hard

print('''Задание-1:
         Матрицы в питоне реализуются в виде вложенных списков:
         Пример. Дано:
         matrix = [[1, 0, 8],
                   [3, 4, 1],
                   [0, 4, 2]]
          
         Выполнить поворот (транспонирование) матрицы
         Пример. Результат:
         matrix_rotate = [[1, 3, 0],
                          [0, 4, 4],
                          [8, 1, 2]]

         Суть сложности hard: Решите задачу в одну строку

      ''')
matrix = [[1, 0, 8],
          [3, 4, 1],
          [0, 4, 2]]
print('\n', [i[0] for i in matrix], '\n', [i[1] for i in matrix], '\n', [i[2] for i in matrix], '\n')
