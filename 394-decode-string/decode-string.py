class Solution:
    def decodeString(self, s: str) -> str:
        number = []
        stack = []
        n = 0
        for item in list(s):
            if item.isdigit():
                n = n*10 + int(item)
            elif item==']':
                string = ""
                while stack and stack[-1]!='[':
                    string = stack.pop() + string
                stack.pop()
                val = number.pop()
                ss = string*val
                stack.append(ss)
            else:
                if n!=0:
                    number.append(n)
                    n = 0
                stack.append(item)
        return "".join(stack)
        # 
        # 300[a]
        # 