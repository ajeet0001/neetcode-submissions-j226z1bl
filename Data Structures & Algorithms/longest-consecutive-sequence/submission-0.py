class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            n = num
            while n in nums:
                n -=1
            ans = max(ans,num-n)
        return ans
        