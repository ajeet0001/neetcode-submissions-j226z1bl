class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [seen[target-nums[i]]+1,i+1]
            seen[nums[i]] = i
        return []


        