import networkx as nx
import bfs
import dfs


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

    # Додавання станцій та зв'язків
    G = nx.Graph()
    for line in [red_line, blue_line, green_line]:
        G.add_nodes_from(line)
        nx.add_path(G, line)

    # Додавання зв'язків через пересадочні станції
    G.add_edge("Театральна", "Золоті ворота")  # Червона <-> Зелена
    G.add_edge("Майдан Незалежності", "Хрещатик")  # Синя <-> Червона
    G.add_edge("Площа Український Героїв", "Палац спорту")  # Синя <-> Зелена

    # конвертуємо граф в словник
    graph_dict = nx.to_dict_of_dicts(G)

    start, end = 'Шулявська', 'Кловська'
    dfs_path = dfs.dfs_iterative(graph_dict, start, end)
    print("DFS Path:")
    print_path(dfs_path)

    print("\nBFS Path:")
    bfs_path = bfs.bfs_iterative(graph_dict, start, end)
    print_path(bfs_path)


def print_path(list):
    str_list = [str(i) for i in list]
    arrow = ' \u2192 '
    joined_string = arrow.join(str_list)
    print(joined_string)


if __name__ == "__main__":
    main()
