class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        n = 0
        l = 0
        for r in range(len(nums)):
            n += nums[r]
            while n>=target:
                n-=nums[l]
                ans = min(ans,r-l+1)
                l+=1
        return 0 if ans == float('inf') else ans