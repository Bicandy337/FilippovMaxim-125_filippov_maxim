import requests
import datetime
import urllib.parse

def season_events(number_of_month, year):
    # Получаем название месяца
    month_name = datetime.date(1900, number_of_month, 1).strftime('%B')
    # Преобразуем русскоязычные символы в URL
    month_url = urllib.parse.quote(month_name)

    # Формируем URL страницы категории месяца и года
    url = f"https://ru.wikipedia.org/wiki/Категория:{month_url}_{year}_года"

    # Отправляем GET-запрос на страницу
    response = requests.get(url)

    # Получаем HTML-код страницы
    html = response.text

    # Ищем ссылки на статьи по подстроке "<a href=\"/wiki"
    start_index = 0
    article_titles = []
    for i in range(5):
        start_index = html.find("<a href=\"/wiki", start_index)
        end_index = html.find("\"", start_index + 9)
        article_url = html[start_index + 9:end_index]
        article_title = urllib.parse.unquote(article_url.split("/")[-1]).replace("_", " ")
        article_titles.append(article_title)
        start_index = end_index

    # Формируем строку для записи в файл
    event_description = ", ".join(article_titles)
    event_string = f"Вы родились в {month_name} в {year} году. {event_description}.\n"

    # Записываем строку в файл
    with open("wiki.txt", "a") as file:
        file.write(event_string)