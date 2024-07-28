import networkx as nx
from collections import deque

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

# Додавання ребер для створення циклу
capitals = list(capitals_coords.keys())
for i in range(len(capitals)):
    G.add_edge(capitals[i], capitals[(i + 1) % len(capitals)])

# Алгоритм DFS
def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Алгоритм BFS
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    while queue:
        (vertex, path) = queue.popleft()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Вибір стартової та кінцевої точки для пошуку шляху
start_city = 'Paris'
goal_city = 'Berlin'

# Знаходження всіх шляхів з Парижа до Берліна за допомогою DFS та BFS
dfs_paths = list(dfs(G, start_city, goal_city))
bfs_paths = list(bfs(G, start_city, goal_city))

print(f"DFS paths from {start_city} to {goal_city}:")
for path in dfs_paths:
    print(path)

print(f"\nBFS paths from {start_city} to {goal_city}:")
for path in bfs_paths:
    print(path)

# Порівняння результатів
print("\nComparison of DFS and BFS results:")
print(f"Number of DFS paths: {len(dfs_paths)}")
print(f"Number of BFS paths: {len(bfs_paths)}")

