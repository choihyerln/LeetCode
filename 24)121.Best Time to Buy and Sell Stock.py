from typing import List

class Solution:
    def maxProfit(prices: List[int]) -> int:
        # 타임아웃
        # arr = []
        # for i in range(len(prices)-1):
        #     for j in range(i+1, len(prices)):
        #         if (prices[i] < prices[j]):
        #             arr.append(prices[j]-prices[i])
        # return 0 if not arr else max(arr)

        min_price = prices[0]
        max_pro = 0
        
        for price in prices:
            new_pro = price - min_price
            if new_pro > max_pro:
                max_pro = new_pro
            if price < min_price:
                min_price = price
        
        return max_pro

a = Solution
prices = [7,1,5,3,6,4]
print(a.maxProfit(prices))