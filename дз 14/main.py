import random


def guess_number():
    # Загадываем число от 1 до 100
    number = random.randint(1, 100)
    # Инициализируем счетчик попыток
    attempts = 0

    # Просим пользователя ввести число до тех пор, пока он не угадает
    while True:
        try:
            guess = int(input("Угадайте число от 1 до 100: "))
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
            continue

        attempts += 1

        if guess == number:
            print(f"Поздравляем! Вы угадали число за {attempts} попыток.")
            name = input("Введите ваше имя: ")
            with open("game.txt", "a") as file:
                file.write(f"{name}: {attempts} попыток\n")
            break
        elif guess < number:
            print("Загаданное число больше.")
        else:
            print("Загаданное число меньше.")


# Запускаем игру
guess_number()