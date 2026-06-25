class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        sett = set(nums)
        res = 0
        for item in sett:
            if item-1 in sett:
                continue
            longest = 1
            while item+1 in sett:
                longest +=1
                item+=1
            res = max(res,longest)
        return res