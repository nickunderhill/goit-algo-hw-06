from collections import deque


def dfs_iterative(graph, start_vertex, end_vertex):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація стека з початковою вершиною та шляхом до неї
    stack = [(start_vertex, [start_vertex])]
    while stack:
        # Вилучаємо вершину і шлях зі стеку
        vertex, path = stack.pop()
        # Якщо кінцеву вершину досягнуто - повертаємо результат
        if vertex == end_vertex:
            return path
        if vertex not in visited:
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини та шлях до стеку
            for next_vertex in reversed(graph[vertex]):
                if next_vertex not in visited:
                    stack.append((next_vertex, path + [next_vertex]))
    return None
