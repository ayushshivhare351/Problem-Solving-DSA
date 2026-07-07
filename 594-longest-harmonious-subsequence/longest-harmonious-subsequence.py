class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for item in nums:
            freq[item]=freq.get(item,0)+1
        res = 0
        for i in range(len(nums)):
            val = freq[nums[i]]
            if nums[i]+1 in freq:
                val += freq[nums[i]+1]
            else:
                continue
            res = max(res,val)
        return res