import random


def magic(X):
    # Генерируем случайную последовательность чисел
    seq = [random.randint(0, 9999) for _ in range(random.randint(5, 100))]

    # Вычисляем сумму чисел последовательности
    seq_sum = sum(seq)

    # Проверяем, можно ли разделить сумму на X без остатка
    if seq_sum % X == 0:
        return True
    else:
        return False