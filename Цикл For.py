# # Вывод элементов списка с помощь цикла
# pigs = ['Ниф-Ниф', 'Наф-Наф', 'Нуф-Нуф']
# print('Дорогие свиньи!')
#
# for pig in pigs:
#     print(pig)
#
# print('приглашаю вас на ужин!')
# print('Любящий вас Волк.')
#
# # Вывод числовых элементов цикла с помощь range
# print('Это первый этаж.')
# # Первый этаж построен, начинайте строить со второго
# for i in range(2, 5):
#     # Здесь вместо многоточий
#     # вставьте номер текущего этажа,
#     # вычислите и вставьте номер предыдущего этажа.
#     print('А это', i, 'этаж, он на один выше, чем этаж', i-1)

# Вывод числовых элементов цикла обратном порядке с помощью reversed
# for i in reversed(range(1, 13)): # отчет начинается со сторого аргумента range, 13 не включается
#     print(i, 'бомм!')
#
# print('C новым годом!')

# Разверните год наоборот: напечатайте месяцы в обратном порядке.
# months = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
#
# for month in reversed(months):
#     print(month)

# Полезная переменная снаружи цикла
bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

for i in range(1, 6):
    # На каждой итерации цикла
    # к переменной bunny_counter будет дописываться
    # очередная цифра, запятая и пробел (чтобы числа в строке не слиплись).
    # Получившееся значение будет присвоено той же переменной bunny_counter
    bunny_counter = bunny_counter + str(i) + ', '

print(bunny_counter + 'вышел зайчик погулять!')


bunny_counter1 = ''
for k in reversed(range(1, 6)):
    bunny_counter1 = bunny_counter1 + str(k) + ', '
bunny_counter1 = 'Тут охотник выбигает и в зайчиков! ' + bunny_counter1 + 'стреляет'
print(bunny_counter1)
