__author__ = 'Пастушенко Андрей'
import os 
import shutil
 
# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
 
# Создание папки
def new_dir(name):
    path = os.path.join(name)
    try:
        os.makedirs(path)
        print('Создана папка ' + name)
    except FileExistsError:
         print('Папка с таким именем уже существует')
          
#for i in range(9):
#    new_dir('{}_{}'.format('dir_', i+1))
 
# Удаление папки
def dir_remove(path_to_remove):
    qustn = input('{} {} {}'.format('Точно удалить ?', path_to_remove, ' Y/N '))
    if qustn == 'y' or qustn == 'Y':
        try:
            os.removedirs(path_to_remove)
            print('Вы успешно удалили ' + path_to_remove)
        except (TypeError, FileNotFoundError):
            print('Не верно указан путь')
    else:
        print('Отмена')
 
#for i in range(9):
#    dir_remove('{}_{}'.format('dir_', i+1))
 
 
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
# содержание папки
def dir_list():
    current_list = [os.listdir()]
    print(current_list)

#dir_list() 

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
# копия текущего фвйла
def copy_file():
    shutil.copy(r'easy05.py', r'easy05-copy.py')

#copy_file()
#dir_list() # Проверяем, что копия создалась

def change_dir(dir_path):
    try:
        os.chdir(dir_path)
        print(os.getcwd() + ' - текущая директория')
    except:
        print(dir_path + ' - такой директории нет')
        
#Проверка работы функции смены папок на моём пк
#dir_path = r'C:\Users\ingener401\Documents\Python-course Git\05 - easy-normal-hard\test'
#change_dir(dir_path)  # Переходим в тестовую папку, которую создал вручную
#dir_list() # Должны увидеть test.txt, который там находится. Если функция смены папки работает.
