class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heappush,heappop
        freq = {}
        for item in nums:
            freq[item]=freq.get(item,0)+1

        h = []
        for item in freq:
            b = freq[item]
            a = item
            heappush(h,(b,a))
            while len(h)>k:
                heappop(h)
        res = []
        for item in h:
            res.append(item[1])
        
        return res