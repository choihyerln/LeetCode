from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
       # 3의 배수이면 Fizz, 5의 배수이면 Buzz
        answer = []
        for i in range(1, n+1):
            if (i % 15 == 0):
                answer.append("FizzBuzz")
            elif (i % 3 == 0):
                answer.append("Fizz")
            elif (i % 5 == 0):
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

a = Solution()
n = 5

print(a.fizzBuzz(n))