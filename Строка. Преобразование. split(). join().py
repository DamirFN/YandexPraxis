print('---------ПРЕОБРАЗОВАНИЕ СТРОКИ ВО МНОЖЕСТВО (SET) И СПИСОК(LIST)---------')
string = 'По Борнео и Ямайке ходит слон в трусах и майке'
new_list = list(string)
new_set = set(string)

# Различные выводы одного и того же на экран
print('Сет из строки: ' + str(new_set))
print('Сет из строки:', str(new_set))
print('Сет из строки:', new_set)
print(f'Сет из строки: {new_set}')
print(f'Список из строки: {new_list}')
print('Список из строки:', new_list)

print()
print('--------------------------------------------------------------------------------------------')

print('---------БУКВЫ ПОД НОМЕРАМИ - ИНДЕКСЫ---------')
monument_string = 'Я памятник себе воздвиг нерукотворный'

index_list = [0, 1, 2, 8, 6, 17, 24]

for i in index_list:
    # На каждой итерации цикла
    # берём из строки monument_string элемент с индексом i и печатаем полученную букву
    print(monument_string[i])

print()
print('--------------------------------------------------------------------------------------------')

print('---------РАЗОБРАТЬ СТРОКУ НА СЛОВА: МЕТОД SPLIT()---------')
milk_str = 'молоковоз'

# Применяем метод split() с аргументом 'о':
new_list = milk_str.split('о')

print(new_list)

print()
print('--------------------------------------------------------------------------------------------')
counter_str = 'Раз-два-три-четыре-пять, вышел зайчик погулять'

# Преобразуем строку в список, а разделителем будет дефис
counter_list = counter_str.split()
print(counter_list)

# Создадим ещё одну строку
blok_str = 'Ночь. Улица. Фонарь. Аптека'
# Разобьём фразу по словам.
# Разделителем будет служить сочетание точки и пробела:
blok_list = blok_str.split()
print(blok_list)

print()
print('--------------------------------------------------------------------------------------------')

print('---------"СМОНТИОВАТЬ" СТРОКУ ИЗ ЭЛЕМЕНТОВ СПИСКА. МЕТОД JOIN()---------')
words_list = ['раз', 'два', 'три', 'четыре', 'пять', 'вышел', 'зайчик', 'погулять']
# Метод join() "склеивает" элементы списка,
# создавая строку, в которой
# элементы исходного списка разделены текстовым символом;
# для разделения применим дефис:
new_string = ' '.join(words_list)
print(new_string)

print()
print('--------------------------------------------------------------------------------------------')

print('---------ЗАДАЧА 1---------')
#    Допишите код функции penult_word() так, чтобы она возвращала третье с конца слово из любой фразы, переданной в
#    аргументе.
quote_1 = 'Работает? Не трогай'
quote_2 = 'Если твой код работает, значит это хороший код'
quote_3 = 'Лень - главное достоинство программиста'

def penult_word(message):
    word_list = message.split()
    return word_list[-3]

# Вызовы функции готовы к работе, не изменяйте их!

# Вызываем функцию penult_word с аргументом quote_1 и печатаем результат её работы.
print(penult_word(quote_1))

# То же, но с аргументом quote_2.
print(penult_word(quote_2))

# То же с аргументом quote_3.
print(penult_word(quote_3))

print()
print('--------------------------------------------------------------------------------------------')

print('---------ЗАДАЧА 2---------')
# В коде приготовлен список запросов к Анфисе queries. Необходимо определить, какие из них адресованы Анфисе, а
# какие — другим людям.
def check_query(query):
# Допишите код тела функции
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'



#  Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

# Напечатаем результат.
# Переберём список вопросов в цикле
for q in queries:
    # Каждый из вопросов передадим аргументом
    # в функцию check_query()
    result = check_query(q)
    # И для каждого вызова напечатаем вопрос и, через дефис - вердикт программы
    print(q, '-', result)

print()
print('--------------------------------------------------------------------------------------------')

print('---------ЗАДАЧА 3---------')
# Анфиса научилась отличать своё имя от других. Теперь надо научить её извлекать суть запроса.
def check_query(query):
    elements = query.split(', ')
    # Напишите код функции
    return elements[-1]

# Дальше следует код, вызывающий вашу функцию; не изменяйте его:
queries = [
    'Анфиса, сколько у меня друзей?',
    'Андрей, ну где ты был?',
    'Андрей, ну обними меня скорей!',
    'Анфиса, кто все мои друзья?'
]

for q in queries:
    result = check_query(q)
    print(q, '—', result)

print()
print('--------------------------------------------------------------------------------------------')

print('---------ЗАДАЧА 4---------')
# Упростим задачу из темы "Словари. Практическое применение перебора на Анфисе"
DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def process_anfisa(query):
    if query == 'Сколько у меня друзей?':
        count = len(DATABASE)

        return 'У тебя ' + str(count) + ' друзей.'
    elif query == 'Кто все мои друзья?':
        # Из словаря DATABASE создайте строку с помощью join();
        # имена друзей разделите запятой и пробелом.
        # Запишите эту строку в переменную friends_string (вместо пустых кавычек).
        friends_string = ', '.join(DATABASE)

        return 'Твои друзья: ' + friends_string
    elif query == 'Где все мои друзья?':
        unique_cities = set(DATABASE.values())
        # Из сета unique_cities создайте строку с помощью join();
        # названия городов разделите запятой и пробелом.
        # Запишите эту строку в переменную cities_string (вместо пустых кавычек).
        cities_string = ', '.join(unique_cities)

        return 'Твои друзья в городах: ' + cities_string
    else:
        return '<неизвестный запрос>'


print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))