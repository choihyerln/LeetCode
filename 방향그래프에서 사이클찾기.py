from collections import defaultdict

def dfs(here, visited, graph):
    # 재귀함수 종료조건
    if visited[here]:           # here가 이미 방문되었고
        if visited[here] == -1: # dfs가 아직 끝나지 않았으므로 사이클
            return True
        return False
    
    visited[here] = -1      # dfs가 아직 끝나지 않음
    for node in graph[here]:
        if dfs(node, visited, graph):   # 시작 정점을 그대로 둔채 dfs로 노드를 계속 탐색하여
            return True
    
    visited[here] = 1   # dfs가 끝났으므로 1로 설정
    return False

def solution():
    N = 7
    edges = [(1,2),(1,5),(2,3),(2,6),(3,4),(5,6),(6,4),(4,7),(7,6)]

    # 그래프 정보 및 진입차수 테이블 초기화
    graph = defaultdict(list)

    for edge in edges:
        # s,e = 시작점, 끝점
        s,e = edge
        graph[s].append(e)  # e를 s의 이웃에 추가
    
    visited = [0] * (N+1)
    # for i in range(1, N+1):
    #     # 사이클이 하나라도 존재하면 사이클이 있는 그래프
    #     if dfs(i, i, visited, graph):
    #         return True
    # return False

    return dfs(2, visited, graph)

print(solution())

# def dfs(node):
#     visited[node] = node_order
#     node_order += 1

#     for i in graph[node]:
#         if visited[i] == -1:    # 방문하지 않았다면
#             dfs(i)              # dfs 드가
#         elif not finished[i]:   # 근데 아직도 dfs가 안끝났어?
#             cycle += 1          # 그럼 사이클 도는겨
    
#     finished[node] = True

# graph = [[] for _ in range(101)]
# visited = [-1] * 101
# finished = [False] * 101
# node_order = 0
# cycle = 0

# print(dfs(0))