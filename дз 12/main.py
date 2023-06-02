


def sum_range(start, end):
    # Проверяем, что start и end - целые числа
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Аргументы функции должны быть целыми числами")

    # Если start > end, меняем их местами
    if start > end:
        start, end = end, start

    # Суммируем числа от start до end
    total = 0
    for i in range(start, end + 1):
        total += i

    return total


print(sum_range(1, 10)) # 55
print(sum_range(10, 1)) # 55 (start и end меняются местами)
print(sum_range(-5, 5)) # 0
print(sum_range(0, 0)) # 0 (одно число в диапазоне)