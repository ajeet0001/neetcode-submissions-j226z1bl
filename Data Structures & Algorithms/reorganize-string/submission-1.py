class Solution:
    def reorganizeString(self, s: str) -> str:
        t = Counter(s)
        if max(t.values())>(len(s)+1)//2:
            return ""
        max_heap = []
        for key , val in t.items():
            heapq.heappush(max_heap,(-val,key))
        heapq.heapify(max_heap)
        res = []
        pre_char = ""
        pre_cnt = 0
        while max_heap:
            val,char = heapq.heappop(max_heap)
            val = -val
            res.append(char)

            if pre_cnt>0:
                heapq.heappush(max_heap,(-pre_cnt,pre_char))
            pre_char = char
            pre_cnt = val-1
        return "".join(res)
