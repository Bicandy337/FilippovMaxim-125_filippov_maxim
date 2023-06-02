
text = input("Введите текст (от 5 слов с пробелами): ")
words = text.split() # разбиваем текст на слова

# находим наиболее часто встречающееся слово
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_common_word = max(word_counts, key=word_counts.get)

# находим самое длинное слово
longest_word = max(words, key=len)

# выводим результаты
print("Наиболее часто встречающееся слово:", most_common_word)
print("Самое длинное слово:", longest_word)
