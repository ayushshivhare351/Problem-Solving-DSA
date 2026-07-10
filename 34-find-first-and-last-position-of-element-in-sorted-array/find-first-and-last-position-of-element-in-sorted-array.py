class Solution:
    def leftmost(self,nums,target):
        i,j,ans= 0,len(nums)-1,-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]<target:
                i = mid+1
            elif nums[mid]>target:
                j = mid-1
            else:
                ans = mid
                j = mid-1
        return ans
                
    def rightmost(self,nums,target):
        i,j,ans= 0,len(nums)-1,-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]<target:
                i = mid+1
            elif nums[mid]>target:
                j = mid-1
            else:
                ans = mid
                i = mid+1

        return ans
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.leftmost(nums,target)
        right = self.rightmost(nums,target)
        return [left,right]