class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        n = len(nums)
        i,j=0,0
        res = float('inf')
        while j<n:
            summ+= nums[j]
            while summ>=target:
                res = min(res,j-i+1)
                summ-=nums[i]
                i+=1
            j+=1
        if res==float('inf'):
            return 0
        return res