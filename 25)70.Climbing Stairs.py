class Solution:
    def climbStairs(n: int) -> int:
        dp = [0] * (n+2)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        if n >= 3:
            for i in range(3, n+1):
                dp[i] = dp[i-2] + dp[i-1]
        return dp[n]

a = Solution
n = 45
print(a.climbStairs(n))