class Solution:
    def maxArea(self, nums: List[int]) -> int:
        ans = 0
        l = 0
        r = len(nums)-1
        while l<=r:
            h = min(nums[l],nums[r])
            area = h*(r-l)
            ans = max(ans,area)
            if nums[l]<nums[r]:
                l+=1
            else:
                r-=1
        return ans