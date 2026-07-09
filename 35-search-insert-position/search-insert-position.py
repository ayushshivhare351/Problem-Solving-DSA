class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        i = 0
        j = len(nums)-1
        while i<=j:
            mid = (i+j)//2
            if nums[mid]==target:
                return mid
            elif target<nums[mid]:
                j=mid-1
            else:
                i=mid+1
        
        return i