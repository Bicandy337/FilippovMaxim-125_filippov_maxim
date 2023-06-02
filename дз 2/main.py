import random

# Создаем два списка случайной длины от 50 до 100
list1 = [random.randint(0, 9999) for _ in range(random.randint(50, 100))]
list2 = [random.randint(0, 9999) for _ in range(random.randint(50, 100))]

# Выводим списки для проверки
print("List 1:", list1)
print("List 2:", list2)

# Создаем множества из списков для быстрого поиска элементов
set1 = set(list1)
set2 = set(list2)

# Находим элементы первого списка, которых нет во втором
result = set1.difference(set2)

# Выводим результат
print("Elements of list 1 that are not in list 2:", list(result))