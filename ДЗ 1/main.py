# Вводим данные
x = float(input("Enter Jerry's speed (m/s): "))
y = float(input("Enter Tom's speed (m/s): "))
s = float(input("Enter initial distance (m): "))

# Вычисляем время, за которое Том догонит Джерри
if y <= x:
    print("Tom cannot catch Jerry.")
else:
    t = s / (y - x)
    print("Tom can catch Jerry in", t, "seconds.")