import networkx as nx
from dijkstra import dijkstra


def main():
    # Кількість станцій метро зменшена для кращого сприйняття візуалізакції
    # Червона гілка
    red_line = ["Шулявська", "Політехнічний інститут",
                "Вокзальна", "Університет", "Театральна", "Хрещатик", "Арсенальна", "Дніпро", "Гідропарк", "Лівобережна"]
    # Синя гілка
    blue_line = ["Почайна", "Тараса Шевченка", "Контрактова площа", "Поштова площа",
                 "Майдан Незалежності", "Площа Український Героїв", "Олімпійська", "Палац Україна", "Либідська", "Деміївська"]
    # Зелена гілка
    green_line = ["Сирець", "Дорогожичі", "Лук'янівська", "Золоті ворота", "Палац спорту", "Кловська", "Печерська", "Звіринецька",
                  "Видубичі"]

    # Додавання станцій та зв'язків із вагами, припустимо, що ваги це час у хвилинах і він дорівнює 3хв для станцій без пересдок
    G = nx.Graph()
    for line in [red_line, blue_line, green_line]:
        for i in range(len(line) - 1):
            G.add_edge(line[i], line[i+1], weight=3)

    # Додавання зв'язків через пересадочні станції
    # Припустимо, що час на пересадку займає в середньому 4хв
    G.add_edge("Театральна", "Золоті ворота", weight=4)  # Червона <-> Зелена
    G.add_edge("Майдан Незалежності", "Хрещатик", weight=4)  # Синя <-> Червона
    G.add_edge("Площа Український Героїв", "Палац спорту",
               weight=4)  # Синя <-> Зелена

    # конвертуємо граф в словник
    graph_dict = nx.to_dict_of_dicts(G)
    shortest_paths = dijkstra(graph_dict, "Хрещатик")

    max_station_name_length = max(len(station) for station in shortest_paths)
    header = f"| {'Станція':<{max_station_name_length}} | хвилини |"
    divider = f"|{'-' * (max_station_name_length + 2)}|---------|"

    print(header)
    print(divider)
    sorted_stations = sorted(shortest_paths.items(), key=lambda item: item[1])
    for tuple in sorted_stations:
        print(f"| {tuple[0]:<{max_station_name_length}} | {tuple[1]:<7} |")


if __name__ == "__main__":
    main()
