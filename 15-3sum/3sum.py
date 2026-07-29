class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res  = []
        def twosum(i,j,target):
            while i<j:
                if nums[i]+nums[j]==target:
                    while i<j and nums[i]==nums[i+1]:
                        i+=1
                    while i<j and nums[j]==nums[j-1]:
                        j-=1
                    res.append([-target,nums[i],nums[j]])
                    i+=1
                    j-=1
                elif nums[i]+nums[j]>target:
                    j-=1
                else:
                    i+=1
                
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            twosum(i+1,len(nums)-1,target)
        return res