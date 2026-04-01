class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # to calc area of n-1 term
        stack = []
        ans = 0
        for i in range(len(heights)):
            if stack:
                while stack and heights[stack[-1]]>heights[i]:
                    idx = stack.pop()
                    h = heights[idx]
                    w = i if not stack else i-stack[-1]-1
                    ans = max(ans,h*w)
                stack.append(i)
            else:
                stack.append(i)
        return ans
                   
                