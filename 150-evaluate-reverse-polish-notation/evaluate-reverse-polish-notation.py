class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in "+-*/":
                stack.append(int(item))
            else:
                if item == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b+a))
                elif item == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b-a))
                elif item == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b*a))
                elif item=='/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
        return stack[0]
