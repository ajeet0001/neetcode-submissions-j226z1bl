class FreqStack:

    def __init__(self):
        self.cnt = {}
        self.max_cnt = 0
        self.stack = {}

    def push(self, val: int) -> None:
        valcnt = self.cnt.get(val,0)+1
        self.cnt[val] = valcnt
        if valcnt > self.max_cnt:
            self.max_cnt = valcnt
            self.stack[valcnt] = []
        self.stack[valcnt].append(val)

    def pop(self) -> int:
        res = self.stack[self.max_cnt].pop()
        self.cnt[res] -= 1
        if not self.stack[self.max_cnt]:
            self.max_cnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()