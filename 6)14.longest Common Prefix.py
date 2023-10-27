from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""

        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] == last[i]):
                ans += first[i]
            else:
                break
        return ans

a = Solution()
strs = ["flower","flow","flight"]

print(a.longestCommonPrefix(strs))