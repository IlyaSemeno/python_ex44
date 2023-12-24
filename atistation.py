import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)

# Создаем словарь для хранения one hot представления
one_hot_encoding = {'robot': [], 'human': []}

# Проходим по каждому элементу списка и преобразуем в one hot представление
for value in lst:
    if value == 'robot':
        one_hot_encoding['robot'].append(1)
        one_hot_encoding['human'].append(0)
    else:
        one_hot_encoding['robot'].append(0)
        one_hot_encoding['human'].append(1)

# Создаем списки для новых столбцов на основе one hot представления
is_robot = one_hot_encoding['robot']
is_human = one_hot_encoding['human']

# Создаем словарь для нового DataFrame без использования get_dumies
new_data = {'is_robot': is_robot, 'is_human': is_human}

# Выводим результат
for key, value in new_data.items():
    print(f"{key}: {value}")