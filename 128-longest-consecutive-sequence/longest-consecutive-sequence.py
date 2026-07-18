class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        if len(nums)==0:
            return 0
        longest = 1
        for item in sett:
            if not item-1 in sett:
                count = 1
                val = item+1
                while val in sett:
                    count+=1
                    val+=1
                longest = max(longest, count)
            
        return longest
        