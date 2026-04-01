class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        count_t = {}
        win = {}
        have = 0
        
        res = [-1,-1]
        l = 0
        res_len = float('inf')
        for c in t:
            count_t[c] = count_t.get(c,0)+1
        need = len(count_t)
        for r in range(len(s)):
            char = s[r]
            win[char] = win.get(char,0)+1
            if char in count_t and count_t[char] == win[char]:
                have += 1
            while have==need:
                if  res_len > r-l+1:
                    res_len = r-l+1
                    res = [l,r]
                c = s[l]
                win[c] -= 1
                if c in count_t and count_t[c]>win[c]:
                    have -= 1   
                l+=1
        l,r = res
        return s[l:r+1] if res_len != float('inf') else ""
                      