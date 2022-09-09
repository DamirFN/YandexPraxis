print('---------ЗАДАЧА 1---------')
def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    summ = 0
    for i in listened:
        summ += i
    sum_min = summ // 60
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {sum_min} минут.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    # Напишите код функции calc_stat()
    return f'Вы прослушали {len(listened)} песен общей продолжительностью {round((sum(listened))/60)} минут.'
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))

DATABASE = {
    'Серёга': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}

print()
print('--------------------------------------------------------------------------------------------')

print('---------ЗАДАЧА 2---------')
# Новая функция, она возвращает правильное словосочетание, склоняя слово "друзья"
# в зависимости от того, какое число передано в аргументе friends_count
def format_friends_count(friends_count):
    if friends_count == 1:
        return '1 друг'
    elif 2 <= friends_count <= 4:
        return f'{friends_count} друга'
    else:
        return f'{friends_count} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        # Вызовите функцию format_friends_count() и передайте в неё count.
        # Отредактируйте строку ниже: в ней должно использоваться выражение,
        # которое вернёт функция format_friends_count()
        return f'У тебя {format_friends_count(count)}.'

    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_query(query):
    process = query.split(', ')
    if process[0] == 'Анфиса':
        return process_anfisa(process[1])
    else:
        return process_friend(process[0], process[1])


def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))