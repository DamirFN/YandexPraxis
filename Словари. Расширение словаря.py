# Добавление нового элемента в словарь
english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

# Добавим в словарь english новый элемент "new_words" и ключ "new_words"
english['new_words'] = 'new_words'

# Посмотрим, что теперь хранится в словаре english
print(english)

print('--------------------------------------------------------------------------------------------')

# Одновременное добавление нескольких элементов
english = {
    'рука': 'arm',
    'нога': 'leg',
    'хвост': 'tail',
    'питон': 'python',
    'бэкенд-разработчик': 'back-end developer',
    'голова': 'head'
}

# Объявим новый словарь
new_words = {'мозг': 'brain', 'логика': 'logic'}

# Добавим в словарь english элементы словаря new_words, используем метод update
english.update(new_words)

# Посмотрим, что теперь хранится в словаре english
print(english)

# Заодно выясним, что произошло со словарём new_words
print(new_words)