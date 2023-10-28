# 하위배열의 합이 k와 같다.
# 정수 배열 nums와 정수가 주어지면 합계가 k와 같은 하위 배열의 총 개수를 반환한다.
# 하위 배열은 배열 내 비어있지 않은 연속된 요소 시퀀스

from typing import List
import collections

class Solution:
    def subarraySum(nums: List[int], k: int) -> int:
        # res = 0         # 부분배열 개수
        # prefix_sum = 0  # 누적 합계 저장하는 변수
        # # 누적 합계의 각 특정 값이 몇 번 발생했는지 추척하는 딕셔너리
        # d = {0 : 1}     # = 합이 0이 되는 경우 하나 (초기화)

        # for num in nums:
        #     prefix_sum += num  # 누적합계 업데이트

        #     # prefix_sum - k == 0이면 계산 끝
        #     if prefix_sum - k in d:
        #         res += d[prefix_sum-k]
        #     if prefix_sum not in d:
        #         d[prefix_sum] = 1
        #     else:
        #         d[prefix_sum] += 1
        # return res

        sum_list = collections.Counter()
        # sum-k=0 (누적합 구하기 성공) 인 경우를 위해
        sum_list[0] = 1
        prefix_sum = 0
        res = 0

        for num in nums:
            prefix_sum += num

            # 만약 이전의 누적합 중 prefix_sum-k와 같은 값이 존재한다면
            # 합이 K인 subarray가 존재한다는 의미
            res += sum_list[prefix_sum-k]

            sum_list[prefix_sum] += 1

        return res

a = Solution
nums = [1,2,1,3]
k=3
print(a.subarraySum(nums, k))