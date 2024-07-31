import random

# Граф з попереднього завдання
capitals_coords = {
    "Vienna": (16.3738, 48.2082),
    "Brussels": (4.3517, 50.8503),
    "Sofia": (23.3219, 42.6977),
    "Zagreb": (15.9819, 45.8150),
    "Prague": (14.4378, 50.0755),
    "Copenhagen": (12.5683, 55.6761),
    "Tallinn": (24.7535, 59.4370),
    "Helsinki": (24.9384, 60.1699),
    "Paris": (2.3522, 48.8566),
    "Berlin": (13.4050, 52.5200),
    "Athens": (23.7275, 37.9838),
    "Budapest": (19.0402, 47.4979),
    "Reykjavik": (-21.8277, 64.1265),
    "Dublin": (-6.2603, 53.3498),
    "Rome": (12.4964, 41.9028),
    "Riga": (24.1052, 56.9496),
    "Vilnius": (25.2797, 54.6872),
    "Luxembourg": (6.1296, 49.8153),
    "Amsterdam": (4.9041, 52.3676),
    "Oslo": (10.7522, 59.9139),
    "Warsaw": (21.0122, 52.2297),
    "Lisbon": (-9.1393, 38.7223),
    "Bucharest": (26.1025, 44.4268),
    "Bratislava": (17.1077, 48.1486),
    "Ljubljana": (14.5058, 46.0569),
    "Madrid": (-3.7038, 40.4168),
    "Stockholm": (18.0686, 59.3293),
    "Bern": (7.4474, 46.9480),
    "London": (-0.1278, 51.5074),
}

# Додавання вузлів для столиць
capitals = list(capitals_coords.keys())

# Створення графа у вигляді словника
graph = {capital: {} for capital in capitals}

# Додавання ребер для створення циклу та ваги ребер
for i in range(len(capitals)):
    # Вага ребра може бути рандомною або розрахованою
    weight = random.randint(1, 10)
    current_city = capitals[i]
    next_city = capitals[(i + 1) % len(capitals)]
    graph[current_city][next_city] = weight
    graph[next_city][current_city] = weight  # Оскільки граф неорієнтований

# Реалізація алгоритму Дейкстри без використання бібліотек
def dijkstra(graph, start):
    # Ініціалізація відстаней та попередників
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited_nodes = set(graph.keys())
    
    while unvisited_nodes:
        # Вибір вузла з найменшою відстанню
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)
        
        # Оновлення відстаней до сусідів
        for neighbor, weight in graph[current_node].items():
            if neighbor in unvisited_nodes:
                new_distance = distances[current_node] + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
    
    return distances, previous_nodes

# Функція для знаходження найкоротшого шляху
def find_shortest_path(previous_nodes, target):
    path = []
    while target is not None:
        path.append(target)
        target = previous_nodes[target]
    return path[::-1]

# Вибір стартового вузла
start_city = 'Paris'

# Знаходження найкоротших шляхів від стартового вузла
distances, previous_nodes = dijkstra(graph, start_city)

# Виведення результатів
for target_city in capitals:
    if target_city != start_city:
        path = find_shortest_path(previous_nodes, target_city)
        print(f"Shortest path from {start_city} to {target_city}:")
        print(f"Path: {path}, Length: {distances[target_city]}\n")
