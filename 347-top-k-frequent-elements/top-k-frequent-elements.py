class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = {}
        for item in nums:
            freq[item]=freq.get(item,0)+1

        arr = [[] for _ in range(n+1)]
        
        for item in freq:
            arr[freq[item]].append(item)

        res = []
        for i in range(n,-1,-1):
            if len(arr[i])==0:
                continue
            while len(arr[i])>0 and k>0:
                x = arr[i].pop()
                res.append(x)
                k-=1
        return res