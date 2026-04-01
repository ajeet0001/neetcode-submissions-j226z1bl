class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) ==0:
            return ""
        count_t = Counter(t)
        count_w = {}
        req = len(count_t)
        formed = 0
        min_len = float('inf')
        min_win = ""
        l = 0
        for r in range(len(s)):
            char = s[r]
            count_w[char] = count_w.get(char,0)+1
            if char in count_t and count_t[char]==count_w[char]:
                formed+=1
            while formed ==req:
                if min_len>r-l+1:
                    min_len = r-l+1
                    min_win = s[l:r+1]
                # shrink the window from left while formed == req
                ch = s[l]
                count_w[ch]-=1
                if ch in count_t and count_t[ch]>count_w[ch]:
                    formed-=1
                l+=1
        return min_win 
