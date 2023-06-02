def search_substr(subst, st):
    if subst.lower() in st.lower():
        return "Есть контакт!"
    else:
        return "Мимо!"

subst = "контакт"
st = "Найти КОНТАКТ в строке"
result = search_substr(subst, st)
print(result)
