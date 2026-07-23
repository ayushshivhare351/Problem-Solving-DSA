class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1 and len(trust)==0:
            return 1
        ind = [0]*(n+1)
        out = [0]*(n+1)
        for item in trust:
            a,b = item[0],item[1]
            ind[b]+=1
            out[a]+=1
        for i in range(n+1):
            if ind[i]==n-1 and out[i]==0:
                return i
        return -1