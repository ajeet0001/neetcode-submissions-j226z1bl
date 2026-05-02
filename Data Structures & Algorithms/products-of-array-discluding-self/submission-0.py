class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*(len(nums))
        pre_prod = 1
        for i in range(len(nums)):
            res[i] = pre_prod
            pre_prod *= nums[i]
        suff_prod = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= suff_prod
            suff_prod *= nums[i]
        return res
    