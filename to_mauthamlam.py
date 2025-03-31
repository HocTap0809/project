from typing import List, Tuple


GRAPH = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0]
]


def greedy_coloring(graph: List[List[int]]) -> Tuple[List[int], int]:
    """Thuật toán tô màu tham lam."""
    n = len(graph)
    colors = [-1] * n
    colors[0] = 0

    for u in range(1, n):

        used_colors = {colors[v] for v in range(n) if graph[u][v] == 1 and colors[v] != -1}
        color = 0
        while color in used_colors:
            color += 1
        colors[u] = color

    return colors, max(colors) + 1


def print_results(colors: List[int]):
    color_names = ["Red", "Green", "Blue", "Yellow", "Purple"]
    print("\nKết quả tô màu Greedy:")
    for i, color in enumerate(colors):
        print(f"  Đỉnh {i}: {color_names[color]} (Màu {color})")
    print(f"  Tổng số màu: {max(colors) + 1}")


if __name__ == "__main__":
    print("Đồ thị mẫu (5 đỉnh):")
    for row in GRAPH:
        print(" ", row)

    colors, num_colors = greedy_coloring(GRAPH)
    print_results(colors)