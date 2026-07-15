from functools import cmp_to_key
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for item in words:
            freq[item]=freq.get(item,0)+1
        
        def compare(p, q):
            # If frequencies are different, we want the higher frequency first
            if p[1] != q[1]:
                return -1 if p[1] > q[1] else 1
            # If frequencies are the same, we want alphabetical order (e.g., "i" before "love")
            else:
                return -1 if p[0] < q[0] else 1

        arr = []
        for item in freq:
            arr.append([item,freq[item]])
        
        res = sorted(arr,key=cmp_to_key(compare))

        ans = []
        for i in range(k):
            ans.append(res[i][0])

        return ans
        