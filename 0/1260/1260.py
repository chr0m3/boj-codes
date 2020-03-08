import collections
import sys
import time

input = sys.stdin.readline


def find_next(n: int, v: int, graph: list, visited: list):
    for i in range(1, n + 1):
        if graph[v][i] is True and visited[i] is False:
            # Connected and not visited.
            return i

    return None


def dfs(n: int, v: int, graph: list) -> list:
    visited = [False for _ in range(n + 1)]

    order = list()
    path = list()

    current = v
    while True:
        if visited[current] is False:
            order.append(current)
            visited[current] = True

        # Find and move to next vertex.
        next = find_next(n, current, graph, visited)
        if next is not None:
            path.append(current)
            current = next
            continue

        # DFS finished.
        if len(path) == 0:
            break

        # Backtrack.
        current = path.pop()

    return order


def bfs(n: int, v: int, graph: list) -> list:
    visited = [False for _ in range(n + 1)]

    order = list()
    queue = collections.deque()

    current = v
    while True:
        if visited[current] is True:
            # BFS finished.
            if len(queue) == 0:
                break

            # Move to next vertex.
            current = queue.popleft()
            continue

        visited[current] = True
        order.append(current)

        # Find next vertexes.
        for i in range(1, n + 1):
            if graph[current][i] is True:
                queue.append(i)

    return order


if __name__ == '__main__':
    n, m, v = map(int, input().split())

    graph = [[False for _ in range(n + 1)] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True

    print(' '.join(map(str, dfs(n, v, graph))))
    print(' '.join(map(str, bfs(n, v, graph))))
