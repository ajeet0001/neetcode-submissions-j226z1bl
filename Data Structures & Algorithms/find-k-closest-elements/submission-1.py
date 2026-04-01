class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = []
        for num in arr:
            d = abs(num-x)
            dist.append([num,d])
        dist_sorted = sorted(dist, key = lambda x:x[1])
        ans = []
        a = 0
        for item in dist_sorted:
            ans.append(item[0])
            a +=1
            if a==k:
                break
        ans.sort()
        return ans
        