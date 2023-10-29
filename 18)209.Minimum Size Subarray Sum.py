# 합이 target이 되는 최소 배열 길이

from typing import List
import collections

class Solution:
    def minSubArrayLen(target: int, nums: List[int]) -> int:
        left = 0
        prefix_sum = 0
        res = 1e9

        for i in range(len(nums)):
            prefix_sum += nums[i]
            while prefix_sum >= target:
                res = min(res, i-left+1)
                prefix_sum -= nums[left]
                left += 1
        
        return res if res != 1e9 else 0

a = Solution
target = 7
nums = [2,3,1,2,4,3]
print(a.minSubArrayLen(target, nums))