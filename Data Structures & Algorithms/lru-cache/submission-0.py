class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.count = 0

    def get(self, key: int) -> int:
        if key in self.d:
            val = self.d[key]
            del self.d[key]
            self.d[key] = val
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            self.d[key] = value
        elif self.cap == self.count:
            LRU_key = next(iter(self.d))
            del self.d[LRU_key]
            self.d[key]=value
        else:
            self.d[key]=value
            self.count +=1

