class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a:
            max_heap.append((-a,'a'))
        if b:
            max_heap.append((-b,'b'))
        if c:
            max_heap.append((-c,'c'))
        heapq.heapify(max_heap)
        res = []
        while max_heap:
            val,char = heapq.heappop(max_heap)
            val = -val
            if len(res)>=2 and res[-1]==char and res[-2]==char:
                if not max_heap:
                    break
                val2,char2 = heapq.heappop(max_heap)
                val2 = -val2
                res.append(char2)
                val2 -= 1
                if val2>0:
                    heapq.heappush(max_heap,(-val2,char2))
                heapq.heappush(max_heap,(-val,char))
            else:
                if val>=2:
                    res.append(char)
                    res.append(char)
                    val -= 2
                else:
                    res.append(char)
                    val -= 1
                if val>0:
                    heapq.heappush(max_heap,(-val,char))
        return ''.join(res) 