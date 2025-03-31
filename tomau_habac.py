from typing import List, Tuple
GRAPH = [
    [0, 1, 1, 0, 0],  # Đỉnh 0 kề 1, 2
    [1, 0, 1, 1, 0],  # Đỉnh 1 kề 0, 2, 3
    [1, 1, 0, 1, 0],  # Đỉnh 2 kề 0, 1, 3
    [0, 1, 1, 0, 1],  # Đỉnh 3 kề 1, 2, 4
    [0, 0, 0, 1, 0]  # Đỉnh 4 kề 3
]
def dsatur_coloring(graph: List[List[int]]) -> Tuple[List[int], int]:
    n = len(graph)
    degrees = [sum(row) for row in graph]
    saturation = [0] * n
    colors = [-1] * n

    for _ in range(n):
        max_sat = -1
        selected = -1
        for u in range(n):
            if colors[u] == -1:
                if saturation[u] > max_sat or (saturation[u] == max_sat and degrees[u] > degrees[selected]):
                    max_sat = saturation[u]
                    selected = u
        used_colors = {colors[v] for v in range(n) if graph[selected][v] == 1 and colors[v] != -1}
        color = 0
        while color in used_colors:
            color += 1
        colors[selected] = color
        for v in range(n):
            if graph[selected][v] == 1 and colors[v] == -1:
                saturation[v] += 1

    return colors, max(colors) + 1


def print_results(colors: List[int]):
    """In kết quả tô màu."""
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple"]
    print("\nKết quả tô màu DSatur:")
    for i, color in enumerate(colors):
        print(f"  Đỉnh {i}: {color_names[color]} (Màu {color})")
    print(f"  Tổng số màu: {max(colors) + 1}")
if __name__ == "__main__":
    print("Đồ thị mẫu (5 đỉnh):")
    for row in GRAPH:
        print(" ", row)

    colors, num_colors = dsatur_coloring(GRAPH)
    print_results(colors)