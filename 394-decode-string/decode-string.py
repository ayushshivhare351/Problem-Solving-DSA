class Solution:
    def decodeString(self, s: str) -> str:
        from collections import deque
        stack = deque()
        number = deque()
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            elif ch == "[":
                number.append(num)
                num = 0
                stack.append(ch)
            elif ch != ']':
                stack.append(ch)
                
            else:
                strr = ""
                while stack:
                    res = stack.pop()
                    if res == "[":
                        n = number.pop()
                        stack.append(n*strr)
                        break
                    strr = res + strr
                
        final = ""
        while stack:
            final = stack.pop() + final
        return final