def count_words(text):
    # Проверяем, что text - строка и ее длина не превышает 800 символов
    if not isinstance(text, str) or len(text) > 800:
        raise ValueError("Аргумент функции должен быть строкой длиной не более 800 символов")

    # Разбиваем строку на слова и считаем их количество
    words = text.split()
    return len(words)
print(count_words("привет мир")) # 2
print(count_words("это тестовая строка")) # 3
print(count_words(" ")) # 0 (пустая строка)

