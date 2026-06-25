class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        prefix = 0
        res = 0
        for item in nums:
            prefix+=item
            if prefix-k in freq:
                res += freq[prefix-k]
            freq[prefix]=freq.get(prefix,0)+1
        return res