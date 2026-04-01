class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if stack:
                if char == '+':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x+y)
                elif char == '-':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y-x)
                elif char == '*':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(x*y)
                elif char == '/':
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(int(y/x))
                else:
                    x = int(char)
                    stack.append(x)
            else:
                x = int(char)
                stack.append(x)
        return stack[-1]
