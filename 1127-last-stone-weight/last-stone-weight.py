class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappop,heappush
        heap = []
        for item in stones:
            heappush_max(heap,item)
        while len(heap)>1:
            high = heappop_max(heap)
            low = heappop_max(heap)
            if low==high:
                continue
            else:
                heappush_max(heap,high-low)
        if heap:
            return heap[0]
        return 0