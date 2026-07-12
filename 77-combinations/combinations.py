class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        def solve(start,k,temp):
            if k==0:
                res.append(temp.copy())
                return
            if start>n:
                return

            temp.append(start)
            solve(start+1,k-1,temp)

            temp.pop()
            solve(start+1,k,temp)
        solve(1,k,temp)
        return res
        