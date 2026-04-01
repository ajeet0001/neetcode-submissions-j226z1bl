class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in range(len(operations)):
            if operations[i] == '+':
                x = stack[-1]
                y = stack[-2]
                stack.append(x+y)
            elif operations[i]=='C':
                stack.pop()
            elif operations[i] == 'D':
                x = stack[-1]
                stack.append(2*x)
            else:
                x = int(operations[i])
                stack.append(x)
        return sum(stack)