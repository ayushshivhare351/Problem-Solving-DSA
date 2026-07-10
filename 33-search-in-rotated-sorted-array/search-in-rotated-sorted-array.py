class Solution:
    def pivot(self,nums):
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]>nums[r]:
                l = mid+1
            else :
                r  = mid
        return r
        
    def binary(self,nums,i,j, target):
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                j=mid-1
            else:
                i=mid+1 
        return -1
    def search(self, nums: List[int], target: int) -> int:
        ind = self.pivot(nums)
        a = self.binary(nums,0,ind-1,target)
        b = self.binary(nums,ind,len(nums)-1,target)
        if a==-1 and b==-1:
            return -1
        elif b==-1:
            return a
        elif a==-1:
            return b