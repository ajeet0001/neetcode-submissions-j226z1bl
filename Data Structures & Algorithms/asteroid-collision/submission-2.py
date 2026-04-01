class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for num in asteroids:
            if num>0:
                s.append(num)
            else:
                survive = True
                while s and s[-1]>0 and survive:
                    if s[-1]>abs(num):
                        survive = False
                    elif s[-1]==abs(num):
                        s.pop()
                        survive = False
                    else:
                        s.pop()
                if survive:
                    s.append(num)

        return s
