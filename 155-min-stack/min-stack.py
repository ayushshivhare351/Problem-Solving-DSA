class MinStack:

    def __init__(self):
        self.st =  []
        self.l = 0

    def push(self, value: int) -> None:
        if self.l==0:
            self.st.append([value,value])
            self.l+=1
            return 
        else:
            if self.st[-1][1]>value:
                self.st.append([value,value])
                self.l+=1
            else:
                self.st.append([value,self.st[-1][1]])
            self.l+=1

    def pop(self) -> None:
        if self.l>0:
            self.st.pop()
            self.l-=1
        return

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        if self.l>0:
            return self.st[-1][1]
        return 


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()