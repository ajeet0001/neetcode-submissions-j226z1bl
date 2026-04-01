class MinStack:

    def __init__(self):
        self.s = []
        self.s_min = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.s_min and self.s_min[-1]>=val:
            self.s_min.append(val)
        if len(self.s_min) == 0:
            self.s_min.append(val)
        

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.s_min[-1]:
            self.s_min.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.s_min[-1]
