class Solution:
    def isPalindrome(self, x: int) -> bool:
    # 1. 숫자 1이면 무조건 팰린드롬
    # 2. 숫자 2이상이면 일단 arr에 넣고 짝수 홀수 비교
        if x < 0:
            return False
        
        arr = list(reversed(str(x)))

        if int(''.join(arr)) == x:
            return True
        else:
            return False
    
a = Solution()
x = 121

print(a.isPalindrome(x))