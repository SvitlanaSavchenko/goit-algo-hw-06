import networkx as nx
import random

# Граф з попереднього завдання
G = nx.Graph()
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
for capital in capitals_coords:
    G.add_node(capital, pos=capitals_coords[capital])

# Додавання ребер для створення циклу та ваги ребер
capitals = list(capitals_coords.keys())
for i in range(len(capitals)):
    # Вага ребра може бути рандомною або розрахованою
    weight = random.randint(1, 10)
    G.add_edge(capitals[i], capitals[(i + 1) % len(capitals)], weight=weight)

# Функція для виведення найкоротших шляхів
def find_shortest_paths(graph, start_node):
    # Використання алгоритму Дейкстри для знаходження найкоротших шляхів
    lengths, paths = nx.single_source_dijkstra(graph, start_node)
    
    # Виведення результатів
    for target_node in paths:
        print(f"Shortest path from {start_node} to {target_node}:")
        print(f"Path: {paths[target_node]}, Length: {lengths[target_node]}\n")

# Вибір стартового вузла
start_city = 'Paris'

# Знаходження найкоротших шляхів від стартового вузла
find_shortest_paths(G, start_city)
