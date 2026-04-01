class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if s == " ":
            return 1
        if n == 1:
            return 1
        ans = 0 
        i = 0
        res = ''
        while i<n:
            k = 0
            if s[i] not in res:
                res += s[i]
                i+=1
                k = len(res)
            
            else:
                
                i = i - len(res)+1
                res = ''
            ans = max(k,ans)   
        return ans