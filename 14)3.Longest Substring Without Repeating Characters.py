# 반복되는 문자가 없는 가장 긴 부분 문자열

class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        arr = []
        for i in s:
            arr.append(i)
        
        res = []
        string = ''
        for i in range(1, len(arr)):
            if arr[i-1] != arr[i]:
                string += arr[i-1]
                continue

            if arr[i-1] == arr[i]:
                res.append(string)
                i += 1
                continue

        return string

a = Solution
s = "pwwkew"
print(a.lengthOfLongestSubstring(s))