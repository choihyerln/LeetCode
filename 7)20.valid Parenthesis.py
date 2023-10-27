
class Solution:
    def isValid(s: str) -> bool:
        # while ("()" in s or "[]" in s or "{}" in s):
        #     s = s.replace('()','').replace('[]','').replace('{}','')
        # if not s:
        #     return True
        # else:
        #     return False
    
        while ("()" in s or "[]" in s or "{}" in s):
            if "()" in s:
                s = s.replace('()','')
            
            if "[]" in s:
                s = s.replace('[]','')
            
            if "{}" in s:
                s = s.replace('{}','')

        if not s:
            return True
        else:
            return False

a = Solution
s = "[]]"
print(a.isValid(s))