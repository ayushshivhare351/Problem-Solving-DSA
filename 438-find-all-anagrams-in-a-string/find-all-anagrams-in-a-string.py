class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        def allzero(freq):
            for val in freq.values():
                if val != 0:
                    return False
            return True

        freq = {}
        for item in p:
            freq[item]=freq.get(item,0)+1

        res = []

        i=0
        for j in range(len(s)):
            if s[j] in freq:
                freq[s[j]]-=1
            else:
                freq[s[j]]=-1

            if(j-i+1)==len(p):
                if allzero(freq):
                    res.append(i) 
                
                freq[s[i]]+=1
                i+=1
        return res