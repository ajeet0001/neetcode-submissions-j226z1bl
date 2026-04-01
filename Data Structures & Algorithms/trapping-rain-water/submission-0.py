class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        l_max=r_max=w = 0
        while l<=r:
            if l_max<=r_max:
                l_max = max(l_max,height[l])
                w += l_max - height[l]
                l+=1
            else:
                r_max = max(r_max,height[r])
                w += r_max - height[r]
                r -= 1
        return w