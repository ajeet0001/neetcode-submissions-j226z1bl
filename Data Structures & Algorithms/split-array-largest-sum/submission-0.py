class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(target):
            currsum = 0
            subarr = 0
            for n in nums:
                currsum +=n
                if currsum>target:
                    subarr+=1
                    currsum = n
            return subarr+1 <= k
        l = max(nums)
        r = sum(nums)
        res = r
        while l<=r:
            mid = (l+r)//2
            if canSplit(mid):
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res