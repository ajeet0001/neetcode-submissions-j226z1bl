class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        l =  0
        f1 = {}
        f2 = {}
        for i in range(len(s1)):
            f1[s1[i]] = f1.get(s1[i],0)+1
        for i in range(len(s1)):
            f2[s2[i]] = f2.get(s2[i],0)+1
        if f1 == f2:
            return True
        for r in range(len(s1),len(s2)):
            f2[s2[r]] = f2.get(s2[r],0)+1
            char = s2[l]
            f2[char] -=1
            if f2[char] ==0:
                del f2[char]
            if f1 == f2:
                return True
            l+=1
        return False
