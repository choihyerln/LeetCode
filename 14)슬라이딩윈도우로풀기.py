class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        res = 0
        uniqe_str = set() # 현재 윈도우에 있는 문자들 저장
        left = 0    # 윈도우 왼쪽 경계

        for right in range(len(s)):
            while s[right] in uniqe_str:
                # 중복 문자 있으면 오른쪽으로 이동하면서 중복 문자 제거
                uniqe_str.remove(s[left])
                print(f'set: {uniqe_str}')
                left += 1
            
            # 현재 문자를 윈도우에 추가
            uniqe_str.add(s[right])
            print(uniqe_str)

            # 현재 윈도우의 길이를 최대 길이와 비교해서 갱신
            res = max(res, len(uniqe_str))

        return res
    
a = Solution
s = "dvdf"
print(a.lengthOfLongestSubstring(s))
