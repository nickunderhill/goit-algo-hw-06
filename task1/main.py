import networkx as nx
import matplotlib.pyplot as plt


def main():
    G = nx.Graph()

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

    # Додавання станцій та зв'язків
    G = nx.Graph()
    for line in [red_line, blue_line, green_line]:
        G.add_nodes_from(line)
        nx.add_path(G, line)

    # Додавання кольорів вершин згідно з кольором гілки
    node_color_map = []
    for station in G:
        if station in red_line:
            node_color_map.append('red')
        elif station in blue_line:
            node_color_map.append('lightblue')
        elif station in green_line:
            node_color_map.append('green')

    # Додавання зв'язків через пересадочні станції
    G.add_edge("Театральна", "Золоті ворота")  # Червона <-> Зелена
    G.add_edge("Майдан Незалежності", "Хрещатик")  # Синя <-> Червона
    G.add_edge("Площа Український Героїв", "Палац спорту")  # Синя <-> Зелена

    # Додавання кольорів ребер станцій зʼєднаних пересадками
    edge_color_map = {("Хрещатик", "Майдан Незалежності"): "purple",
                      ("Театральна", "Золоті ворота"): "brown",
                      ("Площа Український Героїв", "Палац спорту"): "teal"}
    edge_colors = [edge_color_map[edge]
                   if edge in edge_color_map else "grey" for edge in G.edges()]

    # Візуалізація графу
    plt.figure(figsize=(16, 9))
    options = {
        "node_color": node_color_map,
        "edge_color": edge_colors,
        "font_size": 8,
        "node_size": 1500,
        "width": 3,
        "with_labels": True
    }
    pos = nx.kamada_kawai_layout(G)
    nx.draw(G, pos, **options)
    plt.title("Граф Київського метрополітену")
    plt.show()

    # Аналіз характеристик графу
    print("Кількість вершин (станцій):", G.number_of_nodes())
    print("Кількість ребер (з'єднань між станціями):", G.number_of_edges())
    print("Ступені вершин:")
    for station in G.nodes():
        print(f"Станція {station} має ступінь {G.degree(station)}")


if __name__ == "__main__":
    main()
