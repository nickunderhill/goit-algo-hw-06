from collections import deque


def bfs_iterative(graph, start_vertex, end_vertex):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною та шляхом до неї
    queue = deque([(start_vertex, [start_vertex])])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину і шлях з черги
        vertex, path = queue.popleft()
        # Повертаємо шлях, коли знайдено кінцеву вершину
        if vertex == end_vertex:
            return path
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Проходимося по всіх сусідах поточної вершини
            for next_vertex in graph[vertex]:
                # Якщо сусід ще не відвіданий додаємо його до черги разом з оновленим шляхом
                if next_vertex not in visited:
                    queue.append((next_vertex, path + [next_vertex]))
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited
