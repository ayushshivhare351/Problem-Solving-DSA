class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = ""
        
        def solve(temp,open, close):
            if len(temp)==2*n:
                res.append(temp)
                return

            if open<n:
                solve(temp+"(",open+1,close)
                
            if close<open:
                solve(temp+")",open,close+1)

            
        solve(temp,0,0)
        return res