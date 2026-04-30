class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for s in strs:
            t = list(s)
            t.sort()
            t = ''.join(t)
            if t in ans:
                ans[t].append(s)
            else:
                
                ans[t] = [s]
        res = list(ans.values())
        return res
        



