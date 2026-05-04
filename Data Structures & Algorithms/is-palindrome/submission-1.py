import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        l = 0
        r = len(st)-1
        while l<=r:
            if st[l]!=st[r]:
                return False
            l+=1
            r-=1
        return True