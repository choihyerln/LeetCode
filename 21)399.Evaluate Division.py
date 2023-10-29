from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1. build the graph 
        graph = defaultdict(dict)

        for i in range(len(equations)):
            x,y = equations[i]
            val = values[i]
            graph[x][y] = val
            graph[y][x] = 1.0 / val
        print(graph)

        # Step 2. DFS function
        def dfs (x,y,visited):
            # neither x not y exists
            if x not in graph or y not in graph:
                return -1.0
            
            # x points to y: graph[x][y]
            if y in graph[x]:
                return graph[x][y]
            
            # x에서 다른 노드를 거쳐서 y로 가는 경로가 있는지 확인
            # dfs 이용
            for i in graph[x]:
                if i not in visited:
                    visited.append(i)
                    # tmp에 i에서 y로 가는 경로 저장
                    tmp = dfs(i,y,visited)
                    # y로 가는 경로가 없으면
                    if tmp == -1:
                        continue
                    # y로 가는 경로가 있으면
                    else:
                        return graph[x][i] * tmp
            return -1
        
        # Step 3. Query Processing
        res = []
        for query in queries:
            res.append(dfs(query[0], query[1], list()))
        
        return res

a = Solution
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]