def market_equilibrium(s, d):
    count = 0
    for i in range(len(s)):
        if s[i] == d[i]:
            count += 1
    return count

s = [10, 20, 30, 40, 50]
d = [20, 30, 40, 10, 50]
result = market_equilibrium(s, d)
print(result)
