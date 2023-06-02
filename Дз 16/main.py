import csv
import datetime
import time

# Создаем заголовки для столбцов
headers = ["№", "Дата и время", "Секунда", "Микросекунда"]

# Открываем файл для записи
with open("rows_300.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(headers)  # Записываем заголовки в файл

    for i in range(1, 301):
        # Получаем текущую дату и время
        current_time = datetime.datetime.now()
        # Получаем текущую секунду
        current_second = current_time.second
        # Получаем текущую миллисекунду
        current_microsecond = current_time.microsecond // 1000

        # Создаем строку для записи в файл
        row = [i, current_time, current_second, current_microsecond]

        # Записываем строку в файл
        writer.writerow(row)

        # Искусственно задерживаем выполнение скрипта на 0.01 секунды
        time.sleep(0.01)
