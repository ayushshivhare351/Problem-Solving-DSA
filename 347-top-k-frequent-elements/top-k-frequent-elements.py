class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for item in nums:
            freq[item]=freq.get(item,0)+1
        for j in range(k):
            if len(res)==k:
                break
            n = max(freq.values())
            for item in freq:
                if freq[item]==n:
                    res.append(item)
                    freq[item]=0
        return res