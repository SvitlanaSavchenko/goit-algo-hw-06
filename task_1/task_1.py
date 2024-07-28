import geopandas as gpd
import matplotlib.pyplot as plt
import networkx as nx
from geopy.distance import geodesic

# Список європейських країн та їх столиць, які хотілось би відвідати!)
european_capitals = {
    "Austria": "Vienna",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Croatia": "Zagreb",
    "Czechia": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "Ireland": "Dublin",
    "Italy": "Rome",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Netherlands": "Amsterdam",
    "Norway": "Oslo",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Spain": "Madrid",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "United Kingdom": "London",
}

# Правильний шлях до шейп-файлу
shapefile_path = r"C:\Progects\goit-algo-hw-06\task_1\ne_110m_admin_0_countries.shp"
world = gpd.read_file(shapefile_path)

# Фільтрація даних для отримання європейських країн
europe = world[world['CONTINENT'] == 'Europe']

# Створення графу з столицями
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
for country, capital in european_capitals.items():
    if capital in capitals_coords:
        G.add_node(capital, pos=capitals_coords[capital])

# Додавання ребер для створення циклу
capitals = list(capitals_coords.keys())
for i in range(len(capitals)):
    G.add_edge(capitals[i], capitals[(i + 1) % len(capitals)])

# Візуалізація карти та графу
fig, ax = plt.subplots(figsize=(12, 12))
europe.plot(ax=ax, color='lightgray', edgecolor='black')

# Отримання позицій для відображення
pos = nx.get_node_attributes(G, 'pos')
nx.draw_networkx_nodes(G, pos, node_size=50, node_color='red')
nx.draw_networkx_edges(G, pos, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=12, font_color='darkolivegreen')  

# Встановлення меж для збільшеного відображення Європи
ax.set_xlim(-25, 45)  # межі по довготі
ax.set_ylim(35, 70)   # межі по широті

# Додаємо заголовок
plt.title("Список європейських країн та їх столиць, які хотілось би відвідати!)")

# Відображаємо карту
plt.show()


# Аналіз графа
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Number of nodes (capitals): {num_nodes}")
print(f"Number of edges (connections): {num_edges}")

# Обчислення довжини маршруту
total_distance = 0
route = []
for i in range(len(capitals)):
    city1 = capitals[i]
    city2 = capitals[(i + 1) % len(capitals)]
    coord1 = capitals_coords[city1][::-1]  # Invert to (latitude, longitude)
    coord2 = capitals_coords[city2][::-1]
    distance = geodesic(coord1, coord2).kilometers
    total_distance += distance
    route.append((city1, city2, distance))

# Виведення маршруту
print("\nRoute details:")
for city1, city2, distance in route:
    print(f"From {city1} to {city2}: {distance:.2f} km")

print(f"\nTotal tour distance: {total_distance:.2f} km")