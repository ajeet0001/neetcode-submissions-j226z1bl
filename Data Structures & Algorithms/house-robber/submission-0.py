class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return max(nums)
        rob = []
        skip = []
        for i,num in enumerate(nums):
            if i ==0:
                rob.append(num)
                skip.append(0)
            else:
                rob.append(num+skip[-1])
                skip.append(max(rob[:-1]))
        return max(rob[-1],skip[-1])