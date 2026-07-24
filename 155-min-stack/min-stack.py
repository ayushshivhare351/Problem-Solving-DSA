class MinStack:

    def __init__(self):
        self.st =  []
        self.mn = float('inf')

    def push(self, value: int) -> None:
        if self.st:
            self.mn = min(value,self.mn)
        else:
            self.mn = value
        self.st.append(value)

    def pop(self) -> None:
        self.st.pop()
        if self.st:
            self.mn =min(self.st)

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.mn


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()