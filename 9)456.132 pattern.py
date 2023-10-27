from typing import List

class Solution:
    def find132pattern(nums: List[int]) -> bool:
        min_val = -1e9
        n = len(nums)

        stack = []
        nums.reverse()
        print(nums)     # 2,4,1,3

        for i in range(n):
            if nums[i] < min_val:
                return True
            
            # 스택이 비어있다 = ??
            while stack and stack[-1] < nums[i]:
                min_val = stack.pop()
            stack.append(nums[i])
        return False
    
a = Solution
nums = [3,1,4,2]
print(a.find132pattern(nums))