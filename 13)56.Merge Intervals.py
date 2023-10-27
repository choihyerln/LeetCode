from typing import List

class Solution:
    def merge(intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        
        a = intervals
        a.sort(key=lambda x: (x[0], x[1]))
        res = []
        res.append(a[0])

        for i in range(1, len(a)):
            # 감싼 경우
            if res[-1][1] >= a[i][0] and res[-1][1] >= a[i][1]:
                continue

            # 걸친 경우
            if res[-1][1] >= a[i][0] and res[-1][1] <= a[i][1]:
                res[-1][1] = a[i][1]
                continue
            
            res.append(a[i])

        return res

a=Solution
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(a.merge(intervals))