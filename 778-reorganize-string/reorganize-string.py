class Solution:
    def reorganizeString(self, s: str) -> str:
        from heapq import heappush,heappop,heapify
        freq = {}
        for item in s:
            freq[item]=freq.get(item,0)+1

        heap = []
        heapify_max(heap)
        for item in freq:
            heappush_max(heap,[freq[item],item])

        result = ""
        n = 1
        while heap:
            temp = []
            ss = ""
            for i in range(n+1):
                if heap:
                    l = heappop_max(heap)
                    frequency = l[0]-1
                    ss += l[1]
                    temp.append([frequency,l[1]])
                else:
                    ss += "_"

            for item in temp:
                if item[0]>0:
                    heappush_max(heap,item)
                    
            if len(heap)==0:
                for item in temp:
                    result += item[1]
            else:
                result += ss

        if "_" in result:
            return ""
        return result