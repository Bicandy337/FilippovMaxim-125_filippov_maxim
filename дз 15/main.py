import os

def print_docs(directory):
    for item in os.listdir(directory):
        # Проверяем, является ли элемент файлом
        if os.path.isfile(os.path.join(directory, item)):
            print(item)
        # Если элемент является папкой, рекурсивно вызываем функцию для этой папки
        elif os.path.isdir(os.path.join(directory, item)):
            print_docs(os.path.join(directory, item))

# Пример использования функции
path = "/Users/user/Documents/example_folder"
print_docs(path)
