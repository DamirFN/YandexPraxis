# Приходящие сообщения
for messages_count in range(0, 21):
    if messages_count == 0:
        print('У вас нет новых сообщений')
    elif messages_count == 1:
        print('У вас 1 новое сообщение')
    elif messages_count <= 4:
        print('У вас', str(messages_count), 'новых сообщения')
    else:
        print('У вас', str(messages_count), 'новых сообщений')

# Будильник со временем суток
for current_hour in range(0, 24):
    print("На часах " + str(current_hour) + ":00.")
    # Вместо многоточий напишите код
    if current_hour < 6:
        print('Доброй ночи!')
    elif current_hour < 12:
        print('Доброе утро!')
    elif current_hour < 18:
        print('Добрый день!')
    elif current_hour < 23:
        print('Добрый вечер!')
    else:
        print('Доброй ночи!')