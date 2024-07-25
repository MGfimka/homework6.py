# Работа со словарями:
my_dict = {'Mikhail': 1987, 'Anna': 1989, 'Sergey': 2015, 'Margarita': 2019}
print(my_dict)
print(my_dict['Margarita'])
print(my_dict.get('Stepan', "'Такого ключа нет'"))
my_dict.update({'Svetlana': 1965,
                'Olga': 1963})
print(my_dict)
a = my_dict.pop('Mikhail')
print(a)
#Работа с множествами:
my_set = {1, 2, 3, 4, 3, 2, 1, 'Banan', 3.14, True, (3, 2, 1)}
print(my_set)
print(my_set.add(6))
print(my_set)
print(my_set.discard(1))
print(my_set)