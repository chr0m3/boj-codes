def dfs(vertex):
    global reachable_vertex
    global visited_vertex

    if visited_vertex[vertex] is True:
        return
    visited_vertex[vertex] = True
    reachable_vertex.append(vertex)

    for i in range(0, vertex_num):
        if adjacent_matrix[vertex][i] is True:
            dfs(i)


vertex_num = int(input())
edge_num = int(input())

adjacent_matrix = [[False for x in range(0, vertex_num)] for y in range(0, vertex_num)]
visited_vertex = [False for x in range(0, vertex_num)]

for i in range(0, edge_num):
    s, d = map(lambda x: (int(x) - 1), input().split())
    adjacent_matrix[s][d] = True
    adjacent_matrix[d][s] = True

reachable_vertex = list()

dfs(0)

print(len(reachable_vertex) - 1)
