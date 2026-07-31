class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i =0
        j =0
        n= len(nums)
        k = n-1
        while j<=k:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j]==2:
                nums[k],nums[j]=nums[j],nums[k]
                k-=1
            else:
                j+=1
            
        