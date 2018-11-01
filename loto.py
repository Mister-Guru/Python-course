"""
Лото
 
Правила игры в лото.
 
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
 
Количество бочонков — 90 штук (с цифрами от 1 до 90).
 
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
 
--------------------------
   9 43 62          74 90
2    27    75 78    82
  41 56 63     76      86
--------------------------
"""
 
import random
import sys
 
# Подготавливаем карточки 
ballsinpot = 90
card1 = 15
card2 = 15
balls = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
card1_set = random.sample(game_set, 15)
card2_set = [e for e in game_set if not e in card1_set]
card1_field = [card1_set[:5], card1_set[5:10], card1_set[10:]]
card2_field = [card2_set[:5], card2_set[5:10], card2_set[10:]]
for card1line in card1_field:
    card1line.sort()
    card1line.insert(random.randint(0, 4), ' ')
    card1line.insert(random.randint(0, 5), ' ')
    card1line.insert(random.randint(0, 6), ' ')
    card1line.insert(random.randint(0, 7), ' ')
for card2line in card2_field:
    card2line.sort()
    card2line.insert(random.randint(0, 4), ' ')
    card2line.insert(random.randint(0, 5), ' ')
    card2line.insert(random.randint(0, 6), ' ')
    card2line.insert(random.randint(0, 7), ' ')
 
#Вспомогательные функции
# Функция вывода игровых карточек
def field(с):
    if с == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for line1 in card1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if с == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line2 in card2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
# Функция хода игрока 
def your_turn():
    a = input('Зачеркнуть цифру? (y/n): ')
    if a == 'y':
        if ball in card1_set:
            for i in card1_field:
                try:
                    i.insert(i.index(ball), '><')
                    i.pop(i.index(ball))
                except ValueError:
                    continue
            print('\nOK')
            return 1
        else:
            print('\nИгра закончена')
            sys.exit()
    if a == 'n':
        if ball in card1_set:
            print('\nИгра закончена')
            sys.exit()
        else:
            print('\nOK')
# Функция хода оппонета 
def opps_turn():
    if ball in card2_set:
        for i in card2_field:
            try:
                i.insert(i.index(ball), '><')
                i.pop(i.index(ball))
            except ValueError:
                continue
        return 1
 
#Запуск игры
for ball in balls:
    ballsinpot -= 1
    print('\nНовый бочонок: {} (осталось: {})\n'.format(ball, ballsinpot))
    field(0)
    field(1)
    if your_turn() == 1:
        card1 -= 1
    if opps_turn() == 1:
        card2 -= 1
    if card1 == 0:
        print('\nВы выиграли!')
        sys.exit()
    if card2 == 0:
        print('\nВы проиграли.')
        sys.exit()
    if ballsinpot == 0:
        print('\nИгра закончена')
        sys.exit()
