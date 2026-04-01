class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = Counter(tasks)
        max_heap = []
        for val in t.values():
            max_heap.append(-val)
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            temp = []
            for i in range(n+1):
                if max_heap:
                    val = - heapq.heappop(max_heap)
                    val -= 1
                    if val:
                        temp.append(-val)
                    time+=1
                elif temp:
                    time+=1
            for i in range(len(temp)):
                heapq.heappush(max_heap,temp[i])
        return time
