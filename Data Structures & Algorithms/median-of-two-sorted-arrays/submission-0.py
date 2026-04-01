class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # using trick
        nums = []
        nums.extend(nums1)
        nums.extend(nums2)
        nums.sort()
        l = 0
        r = len(nums)
        if len(nums)%2 == 0:
            idx = r//2
            return (nums[idx-1]+nums[idx])/2
        else:
            idx = r//2
            return nums[idx]