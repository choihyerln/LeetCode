# 반복되는 문자가 없는 가장 긴 부분 문자열

class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        res = 0
        string = ''

        if s == " ":
            return 1

        for i in s:
            # 중복 문자 X
            if i not in string:
                      res = 0
        string = ''

        if s == " ":
            return 1

        for i in s:
            # 중복 문자 X
            if i not in string:
                string += i
                res = max(res, len(string))
                continue
            # 중복 문자 O
            if i in string:
                # 중복문자의 인덱스 저장
                idx = string.index(i)
                 # string을 idx 다음부터 잘라내고 문자 i를 이어붙여 새로운 string 만들기
                string = string[idx+1:] + i
                res = max(len(string), res)  string += i
                res = max(res, len(string))
                continue
            # 중복 문자 O
            if i in string:
                # 중복문자의 인덱스 저장
                idx = string.index(i)
                 # string을 idx 다음부터 잘라내고 문자 i를 이어붙여 새로운 string 만들기
                string = string[idx+1:] + i
                res = max(len(string), res)

        return res

a = Solution
s = "dvdf"
print(a.lengthOfLongestSubstring(s))