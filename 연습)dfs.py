def dfs(graph, start, visited):
    visited[start] = True
    print(start, end='')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
'''
   1 -- 2 -- 7
   |    |
   3 -- 4 -- 5
        |
        6
        |
        8

'''

visited = [0]*len(graph)

dfs(graph, 1, visited)