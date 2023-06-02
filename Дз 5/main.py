
def eqv(a, b, c):
    # Вычисляем точность eps
    eps = 0.0001 * max(a, b)

    # Складываем числа a и b
    sum_ab = a + b

    # Сравниваем сумму с числом c с точностью eps
    if abs(sum_ab - c) <= eps:
        return True
    else:
        return False
result = eqv(12345.67, 9876.54, 22222.21)
print(result) # Выводит True или False в зависимости от значений a, b и c