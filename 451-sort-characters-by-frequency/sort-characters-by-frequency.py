class Solution:
    def frequencySort(self, s: str) -> str:
        f = {}
        for i in s:
            f[i]=f.get(i,0)+1

        res = ""
        mf = max(f.values())
        for j in range(mf,0,-1):
            for ch in f:
                if f[ch]==j:
                    res += ch*j

        return res