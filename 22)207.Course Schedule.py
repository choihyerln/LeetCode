# dfs, cycle이 있으면 false
# 특정 정점에서 출발하여 돌아다니다가 다시 처음 출발했던 곳으로 되돌아 갈 수 있으면 사이클이 있는 것
from typing import List
from collections import defaultdict

class Solution:
    graph = []          # 인접 리스트 그래프
    visited = []        # 방문 여부
    finished = []       # 함수 호출 종료 여부
    cycle = 0           # 사이클 존재 여부

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # init table
        self.visited = [0 for _ in range(numCourses)]
        self.finished = [0 for _ in range(numCourses)]

        # init graph
        self.graph = defaultdict(list)
        
        # prerequisites[i][0]의 부모노드는 prerequisites[i][1]
        for pre in prerequisites:
            x,y = pre
            self.graph[y].append(x)
            print(self.graph)
        
        # 일단 모든 노드를 시작으로 한다.
        for i in range(numCourses):
            self.dfs(i)
            # 사이클이 존재하면
            if self.cycle:
                break
        # 사이클이 존재하지 않음 -> 끝내기!!! (true)
        return not self.cycle
    
    # curr 노드 방문
    def dfs(self, curr):
        print("dfs 호출한 curr: ", curr)
        # 방문했다면 .. (일단 결론은 무조건 return)
        if self.visited[curr]:
            # 이미 curr를 다녀간 dfs 함수가 아직 진행중인데 또 방문함?..
            if self.finished[curr] == 0:
                self.cycle = 1      # 사이클임..
                return
        
        # 방문하지 않았다면 방문처리
        self.visited[curr] = 1
        
        # curr과 연결된 인접 노드들 for문 돌면서 방문
        for i in self.graph[curr]:
            self.dfs(i)
            if self.cycle == 1:
                return 
            # self.visited[curr] = 0
        self.finished[curr] = 1  # curr는 함수 호출 다 했으므로 종료처리
    
a = Solution()
numCourses = 2
prerequisites = [[1,0], [2,0], [3,0]]  # prerequisites[i][1] 들어야만 prerequisites[i][0] 수강 가능
print(a.canFinish(numCourses, prerequisites))