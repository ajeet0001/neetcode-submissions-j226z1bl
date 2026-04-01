class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, num in enumerate(tasks):
            num.append(i)
        tasks.sort()
        min_heap = []
        curr_time = 0
        res = []
        idx = 0
        while idx<len(tasks) or min_heap:
            while idx<len(tasks):
                enqueue_time,prc_time,index = tasks[idx]
                if enqueue_time<=curr_time:
                    heapq.heappush(min_heap,(prc_time,index))
                    idx+=1
                else:
                    break
            if min_heap:
                val = heapq.heappop(min_heap)
                curr_time+=val[0]
                res.append(val[1])
            else:
                curr_time = tasks[idx][0]
        return res
