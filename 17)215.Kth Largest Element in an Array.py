# 배열에서 k번째로 큰 요소

from typing import List
import heapq as hq

class Solution:
    def findKthLargest(nums: List[int], k: int) -> int:
        # heap 사용
        # res = []

        # for i in range(len(nums)):
        #     hq.heappush(res, -nums[i])

        # for i in range(k):
        #     if i==k-1:
        #         return -(hq.heappop(res))
        #     hq.heappop(res)

        # 더 간단한 방법
        hq.heapify(nums)
        # 큰 순서대로 k개 뽑으면 제일 마지막 값이 k번째로 큰 요소
        return hq.nlargest(k, nums)[-1]

a = Solution
nums = [3,2,1,5,6,4]
k = 2
print(a.findKthLargest(nums, k))