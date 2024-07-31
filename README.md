### Завдання 1

Створіть граф за допомогою бібліотеки `networkX` для моделювання певної реальної мережі (наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).

> [!TIP]
> INFO
>
> 📖 Реальну мережу можна вибрати на свій розсуд, якщо немає можливості придумати свою мережу, наближену до реальності.

Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, кількість вершин та ребер, ступінь вершин).

### Завдання 2

Напишіть програму, яка використовує алгоритми `DFS` і `BFS` для знаходження шляхів у графі, який було розроблено у першому завданні.

Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

### Завдання 3

Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.


## Критерії прийняття ДЗ

Прикріплені посилання на репозиторій `goit-algo-hw-06` та безпосередньо самі файли репозиторію у форматі `zip`.

## Використання

 Встановіть необхідні бібліотеки:
    ```
   - pip install networkx
   - pip install geopandas
   - pip install geopy

    ```
    
### Завдання 1:

Створено та візуалізовано граф — модель певної реальної мережі.

Проведено аналіз основних характеристик створеного графа, а також опишемо покроковий маршрут і обчислимо загальну довжину поїздки по столицях. Ось, як це можна зробити:

1. Аналіз основних характеристик графа
Ми можемо використовувати функції з бібліотеки networkx для аналізу графа, такі як:

* Кількість вершин (Number of nodes (capitals)): 29.
* Кількість ребер (Number of edges (connections)): 29.

2. Визначення маршруту та його довжини
Щоб визначити маршрут поїздки по столицях, ми використовуємо вже створений цикл в графі. Довжину поїздки можна приблизно обчислити, якщо розрахувати відстані між координатами кожної столиці.
     * From Vienna to Brussels: 917.34 km
     * From Brussels to Sofia: 1701.41 km
     * From Sofia to Zagreb: 680.46 km
     * From Zagreb to Prague: 487.53 km
     * From Prague to Copenhagen: 635.78 km
     * From Copenhagen to Tallinn: 839.33 km
     * From Tallinn to Helsinki: 82.31 km
     * From Helsinki to Paris: 1912.95 km
     * From Paris to Berlin: 879.70 km
     * From Berlin to Athens: 1803.12 km
     * From Athens to Budapest: 1123.88 km
     * From Budapest to Reykjavik: 3075.58 km
     * From Reykjavik to Dublin: 1492.70 km
     * From Dublin to Rome: 1888.67 km
     * From Rome to Riga: 1867.47 km
     * From Riga to Vilnius: 262.42 km
     * From Vilnius to Luxembourg: 1410.00 km
     * From Luxembourg to Amsterdam: 296.63 km
     * From Amsterdam to Oslo: 914.67 km
     * From Oslo to Warsaw: 1065.30 km
     * From Warsaw to Lisbon: 2764.10 km
     * From Lisbon to Bucharest: 2982.34 km
     * From Bucharest to Bratislava: 806.45 km
     * From Bratislava to Ljubljana: 305.06 km
     * From Ljubljana to Madrid: 1601.64 km
     * From Madrid to Stockholm: 2596.20 km
     * From Stockholm to Bern: 1546.08 km
     * From Bern to London: 748.66 km
     * From London to Vienna: 1238.91 km
      
      **Total tour distance: 37926.67 km.**


### Завдання 2:

Програмно реалізовано алгоритми `DFS` і `BFS` для знаходження шляхів у графі, який було розроблено у першому завданні.

Здійснено порівняння результатів алгоритмів для цього графа, пояснено різницю в отриманих шляхах. Обґрунтовано, чому шляхи для алгоритмів саме такі.

Висновки оформлено у вигляді файлу `readme.md` домашнього завдання.

Порівняння алгоритмів DFS та BFS у графі європейських столиць

Цей проект реалізує та порівнює алгоритми DFS (глибина перший пошук) та BFS (пошук у ширину) для знаходження шляхів у графі, що моделює європейські столиці.

Результати

- **DFS (глибина перший пошук)**:
  - DFS намагається заглибитись у граф, відвідавши кожного сусіда поточного вузла перед тим, як повернутись назад.
  - Цей алгоритм зазвичай знаходить один із можливих шляхів до цілі, який може бути досить глибоким.

- **BFS (пошук у ширину)**:
  - BFS намагається відвідати всі вузли на поточному рівні перш, ніж перейти до наступного рівня.
  - Цей алгоритм зазвичай знаходить найкоротший шлях (у термінах кількості вузлів) до цілі.

Порівняння результатів

Шляхи, знайдені за допомогою DFS та BFS, можуть відрізнятись через різні стратегії обходу графа. BFS зазвичай знаходить найкоротший шлях, тоді як DFS може знайти шлях з більшою кількістю кроків, але він глибший.

**Висновок**

Шляхи для алгоритмів DFS та BFS різняться через їх природу: DFS заглиблюється у граф, а BFS шукає у ширину, що дозволяє знайти найкоротший шлях.

DFS paths from Paris to Berlin:
['Paris', 'Berlin']
['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm', 'Madrid', 'Ljubljana', 'Bratislava', 'Bucharest', 'Lisbon', 'Warsaw', 'Oslo', 'Amsterdam', 'Luxembourg', 'Vilnius', 'Riga', 'Rome', 'Dublin', 'Reykjavik', 'Budapest', 'Athens', 'Berlin']

BFS paths from Paris to Berlin:
['Paris', 'Berlin']
['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm', 'Madrid', 'Ljubljana', 'Bratislava', 'Bucharest', 'Lisbon', 'Warsaw', 'Oslo', 'Amsterdam', 'Luxembourg', 'Vilnius', 'Riga', 'Rome', 'Dublin', 'Reykjavik', 'Budapest', 'Athens', 'Berlin']

Comparison of DFS and BFS results:
Number of DFS paths: 2
Number of BFS paths: 2

### Завдання 3:

У граф додано ваги ребер, програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі.

**Висновок**

Програма реалізує алгоритм Дейкстри для знаходження найкоротших шляхів у графі європейських столиць з випадковими вагами. Цей алгоритм знаходить найкоротші шляхи з урахуванням ваг ребер, що важливо для задачі планування оптимальних маршрутів.

Вибір стартового вузла
start_city = 'Paris'

Shortest path from Paris to Vienna:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna'], Length: 28

Shortest path from Paris to Brussels:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels'], Length: 27

Shortest path from Paris to Sofia:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia'], Length: 20

Shortest path from Paris to Zagreb:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb'], Length: 17    

Shortest path from Paris to Prague:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague'], Length: 10

Shortest path from Paris to Copenhagen:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen'], Length: 6

Shortest path from Paris to Tallinn:
Path: ['Paris', 'Helsinki', 'Tallinn'], Length: 4

Shortest path from Paris to Helsinki:
Path: ['Paris', 'Helsinki'], Length: 1

Shortest path from Paris to Berlin:
Path: ['Paris', 'Berlin'], Length: 4

Shortest path from Paris to Athens:
Path: ['Paris', 'Berlin', 'Athens'], Length: 7

Shortest path from Paris to Budapest:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest'], Length: 8

Shortest path from Paris to Reykjavik:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik'], Length: 11

Shortest path from Paris to Dublin:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin'], Length: 18      

Shortest path from Paris to Rome:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome'], Length: 
19

Shortest path from Paris to Riga:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga'], 
Length: 20

Shortest path from Paris to Vilnius:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius'], Length: 29

Shortest path from Paris to Luxembourg:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg'], Length: 32

Shortest path from Paris to Amsterdam:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'Amsterdam'], Length: 38

Shortest path from Paris to Oslo:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'Amsterdam', 'Oslo'], Length: 42

Shortest path from Paris to Warsaw:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'Amsterdam', 'Oslo', 'Warsaw'], Length: 48

Shortest path from Paris to Lisbon:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'Amsterdam', 'Oslo', 'Warsaw', 'Lisbon'], Length: 54

Shortest path from Paris to Bucharest:
Path: ['Paris', 'Berlin', 'Athens', 'Budapest', 'Reykjavik', 'Dublin', 'Rome', 'Riga', 'Vilnius', 'Luxembourg', 'Amsterdam', 'Oslo', 'Warsaw', 'Lisbon', 'Bucharest'], Length: 57

Shortest path from Paris to Bratislava:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm', 'Madrid', 'Ljubljana', 'Bratislava'], Length: 61

Shortest path from Paris to Ljubljana:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm', 'Madrid', 'Ljubljana'], Length: 56       

Shortest path from Paris to Madrid:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm', 'Madrid'], Length: 55

Shortest path from Paris to Stockholm:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern', 'Stockholm'], Length: 47

Shortest path from Paris to Bern:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London', 'Bern'], Length: 37

Shortest path from Paris to London:
Path: ['Paris', 'Helsinki', 'Tallinn', 'Copenhagen', 'Prague', 'Zagreb', 'Sofia', 'Brussels', 'Vienna', 'London'], Length: 32
