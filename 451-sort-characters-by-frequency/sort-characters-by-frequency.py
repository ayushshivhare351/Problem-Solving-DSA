class Solution:
    def frequencySort(self, s: str) -> str:
        from heapq import heappush,heappop,heapify
        heap = []
        heapify_max(heap)
        freq = {}
        for item in s:
            freq[item]= freq.get(item,0)+1

        for item in freq:
            heappush_max(heap,[freq[item],item])

        res = ""
        while heap:
            temp = []
            ss = ""
            a = heappop_max(heap)
            for i in range(a[0]):
                ss+= a[1]
            res+=ss
        return res
        