class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for item in s:
            freq[item]=freq.get(item,0)+1
        
        for i in range(len(s)):
            if freq[s[i]]==1:
                return i
        return -1