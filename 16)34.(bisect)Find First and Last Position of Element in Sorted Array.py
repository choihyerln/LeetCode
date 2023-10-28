# 오름차순 정렬된 배열에서 요소의 첫 번째와 마지막 위치 찾기
# target 값의 시작 위치와 끝 위치 찾기
# target을 배열에서 찾을 수 없으면 return [-1, -1]
from typing import List
import bisect

class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        # TC: O(n)
        # res = []

        # if target not in nums:
        #     return [-1, -1]

        # for i in nums:
        #     if i == target:
        #         res.append(nums.index(i))
        #         nums.reverse()
        #         break
        
        # for i in nums:
        #     if i == target:
        #         res.append(len(nums)-nums.index(i)-1)
        #         break

        # return res

        # bisect, TC: O(logN)
        if target not in nums:
            return [-1, -1]

        # bisect를 이용해서 왼쪽, 오른쪽 인덱스 구하기
        start = bisect.bisect_left(nums, target)
        end = bisect.bisect_right(nums, target)

        return [start, end-1]

a = Solution
nums = [5,7,7,8,8,10]
target = 8
print(a.searchRange(nums, target))