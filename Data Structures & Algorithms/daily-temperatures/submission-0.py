class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        for i in range(n-1):
            if temperatures[i+1]>temperatures[i]:
                ans[i] = 1
            else:
                j = i+1
                while j<n:
                    if temperatures[j]>temperatures[i]:
                        ans[i] = j-i
                        break
                    j+=1
        return ans