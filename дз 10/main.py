nicknames = ['Мавпродош', 'Лорнектиф', 'Древерол', 'Фиригарпиг', 'Клодобродыч']





def check_nickname(nickname):
    if nickname in nicknames:
        print(f"Ты – свой. Приветствую, любезный {nickname}!")
    else:
        print("Тут ничего нет. Еще есть вопросы?")





nickname = input("Введите свой никнейм: ")
check_nickname(nickname)