class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        min_heap = []
        curr_dist = 0
        cap = 0
        for item in trips:
            num,start,end = item
            # drop of the passesger whose end_time<=start
            while min_heap and min_heap[0][0]<=start:
                e,c = heapq.heappop(min_heap)
                cap -= c
            # pick up the new passenger
            cap += num
            if cap>capacity:
                return False
            heapq.heappush(min_heap,(end,num))
        return True

