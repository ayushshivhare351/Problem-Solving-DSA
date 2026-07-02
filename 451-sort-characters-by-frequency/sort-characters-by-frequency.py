class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for item in s:
            freq[item] = freq.get(item,0)+1
        mx = max(freq.values())
        res = ""
        for i in range(mx,0,-1):
            for ch in freq:
                if freq[ch]== i:
                    res += ch*i
        return res