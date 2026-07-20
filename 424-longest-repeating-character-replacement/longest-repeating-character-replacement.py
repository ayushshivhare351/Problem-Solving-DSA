class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        window = 0
        maxf = -1
        res = 0
        i,j=0,0  
        while j<len(s):
            freq[s[j]]=freq.get(s[j],0)+1
            window = j-i+1
            maxf = max(freq.values())
            if window-maxf<=k:
                res = max(res,window)
            if window-maxf>k:
                window-=1
                freq[s[i]]-=1
                i+=1
            j+=1
        return res
            
            