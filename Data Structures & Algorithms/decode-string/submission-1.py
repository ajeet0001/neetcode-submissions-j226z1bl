class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == ']':
                c = ""
                while stack and stack[-1]!='[':
                    c = stack.pop()+c
                stack.pop()
                num = ''
                while stack and stack[-1].isdigit():
                    
                    num = stack.pop()+num
                st = c * int(num)
                stack.append(st)
            else:
                stack.append(char)
        return ''.join(stack)

