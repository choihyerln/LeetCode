class Solution:
    def reverse(x: int) -> int:
        arr = ''
        l = len(str(x))

        # x가 양수일 때
        if x >= 0:
            for i in str(x):
                arr += i
                res = arr[::-1]
                if int(res) > 2**31 - 1:
                    return 0
            return int(res)
        
        # x가 음수일 때
        else:
            for i in range(1, l):
                arr += (str(x))[i]
                res = '-' + arr[::-1]
                if int(res) < -2**31:
                    return 0
            return int(res)

a = Solution
x = -123
print(a.reverse(x))