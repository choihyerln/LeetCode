from typing import List

class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # start, end 인덱스
            start = i+1
            end = len(nums)-1

            while start < end:
                total = nums[start] + nums[i] + nums[end]
                if total > 0:
                    end -= 1

                elif total == 0:
                    res.append([nums[start],nums[i],nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start += 1

                elif total < 0:  #else
                    start += 1
        return res

a = Solution
nums = [-1,0,1,2,-1,-4]
print(a.threeSum(nums))