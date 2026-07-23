class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        res = []
        maxf = max(freq.values())
        while len(res)!=k:
            for item in freq:
                if freq[item]==maxf:
                    res.append(item)
            maxf-=1
                    
                    
        return res