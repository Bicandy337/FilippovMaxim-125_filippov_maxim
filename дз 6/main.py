def find_best_buyers(x, y, z, cost):
    total_money = [x, y, z]
    total_money.sort(reverse=True)
    if total_money[0] + total_money[1] <= cost:
        return "Ни один из пользователей не может купить подписку"
    elif total_money[0] <= cost:
        return "Только один пользователь может купить подписку"
    else:
        return "Два пользователя могут купить подписку"

x = 100
y = 200
z = 300
cost = 250
result = find_best_buyers(x, y, z, cost)
print(result)