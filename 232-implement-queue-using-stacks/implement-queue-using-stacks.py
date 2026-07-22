class MyQueue:

    def __init__(self):
        self.q = []
        self.l = 0
        

    def push(self, x: int) -> None:
        self.l+=1
        self.q.append(x)
        

    def pop(self) -> int:
        if self.q:
            a = self.q.pop(0)
            self.l-=1
            return a
        

    def peek(self) -> int:
        if self.q:
            return self.q[0] 
        

    def empty(self) -> bool:
        if self.l==0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()