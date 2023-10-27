# 만약 0보다 큰 여는 괄호가 있다면 닫는 괄호로 재귀 호출.
# 만약 0보다 큰 닫는 괄호가 있다면 여는 괄호로 재귀 호출

from typing import List

class Solution:
    def generateParenthesis(n: int) -> List[str]:
        res = []
        def dfs(open, close, s):
            if open==n and close==n:
                res.append(s)
                return
            
            if open < n:
                dfs(open+1, close, s+'(')
            
            if close < open:
                dfs(open, close+1, s+')')

        dfs(0,0,'')
        
        return res
a = Solution
n = 2
print(a.generateParenthesis(n))