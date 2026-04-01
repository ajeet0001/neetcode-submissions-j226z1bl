class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        j = i = 0
        ans = float('inf')
        res = 0
        while i<n+1:
            if res >= target:
                l = i-j
                ans = min(l,ans)
            if res > target:
                res -= nums[j]
                j+=1
            else:
                if i>n-1:
                    i+=1
                else:
                    res += nums[i]
                    i+=1
        if ans == float('inf'):
            return 0
        return ans    