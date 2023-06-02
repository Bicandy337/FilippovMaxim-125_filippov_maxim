import heapq

# Создаем граф, представленный в виде словаря, где ключами являются города, а значениями - словари,
# где ключами являются соседние города, а значениями - стоимость перелета между ними
graph = {
    'A': {'B': 100, 'C': 500},
    'B': {'C': 100},
    'C': {'D': 50},
    'D': {'E': 200},
    'E': {'A': 300}
}

def cheapest_route(start, end):
    # Создаем словарь для хранения стоимости пути до каждого города
    distances = {city: float('inf') for city in graph}
    distances[start] = 0

    # Создаем очередь с приоритетом для поиска кратчайшего пути
    queue = [(0, start)]

    # Ищем кратчайший путь до конечного города
    while queue:
        current_distance, current_city = heapq.heappop(queue)

        # Если мы дошли до конечного города, возвращаем стоимость пути до него
        if current_city == end:
            return current_distance

        # Если стоимость пути до текущего города больше, чем уже найденная стоимость,
        # то пропускаем его и переходим к следующему городу
        if current_distance > distances[current_city]:
            continue

        # Ищем соседние города и обновляем стоимость пути до них, если она меньше текущей стоимости
        for neighbor, neighbor_distance in graph[current_city].items():
            distance = current_distance + neighbor_distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    # Если не удалось найти путь до конечного города, возвращаем -1
    return -1

# Пример использования функции
start = 'A'
end = 'E'
cost = cheapest_route(start, end)
if cost == -1:
    print(f"Не удалось найти путь от {start} до {end}")
else:
    print(f"Стоимость самого дешевого пути от {start} до {end}: {cost}")
