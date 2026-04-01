class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        ans = [0]*len(temperatures)
        for i, num in enumerate(temperatures):
            if s:
                while s and temperatures[s[-1]]<num:
                    j = s.pop()
                    ans[j] = i-j
                s.append(i)
            else:
                s.append(i)
        return ans 
