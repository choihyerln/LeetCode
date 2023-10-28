# 오름차순 정렬된 배열에서 요소의 첫 번째와 마지막 위치 찾기
# target 값의 시작 위치와 끝 위치 찾기
# target을 배열에서 찾을 수 없으면 return [-1, -1]
from typing import List
import bisect

class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        # 이분탐색, TC: O(logN)
        if not nums or target not in nums:
            return [-1, -1]
        
        # 가장 첫 번째로 target 만나는 인덱스 찾기
        def find_first(nums, target):
            # 시작, 끝을 답이 될 수 있는 값으로 설정하지 말 것!
            # 그보다 하나 작고, 하나 큰 값으로 설정하기
            start = -1
            end = len(nums)
            while start+1 < end:
                mid = (start + end) // 2
                if nums[mid] < target:
                    start = mid
                else:
                    end = mid
            return end
        
        # 가장 마지막으로 target 만나는 인덱스 찾기
        def find_last(nums, target):
            start = -1
            end = len(nums)
            while start+1 < end:
                mid = (start + end) // 2
                if nums[mid] <= target:
                    start = mid
                else:
                    end = mid
            return start
        
        first = find_first(nums, target)
        last = find_last(nums, target)

        return [first, last]

a = Solution
nums = [5,7,7,8,8,10]
target = 6
print(a.searchRange(nums, target))