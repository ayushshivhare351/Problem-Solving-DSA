class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from heapq import heappush,heappop,heapify
        freq  = {}
        for item in tasks:
            freq[item]=freq.get(item,0)+1

        times = 0
        heap = []
        heapify_max(heap)

        for item in freq:
            if freq[item]>0:
                heappush_max(heap,freq[item])
        
        while heap:
            temp = []
            for i in range(n+1):
                if len(heap)!=0:
                    frequency = heappop_max(heap)
                    frequency-=1
                    temp.append(frequency)
            
            for item in temp:
                if item>0:
                    heappush_max(heap,item)
            
            if len(heap)==0:
                times += len(temp)
            else:
                times += n+1

        return times
