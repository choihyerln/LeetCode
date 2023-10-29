from collections import deque

def bfs(graph, start, visited):
    # 탐색 시작 노드를 큐에 삽입하고 방문처리
    q = deque([start])
    visited[start] = True

    while q:
        target = q.popleft()
        print(target, end='')
        # 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서
        # 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
        for i in graph[target]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

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

visited = [0] * len(graph)

bfs(graph, 1, visited)