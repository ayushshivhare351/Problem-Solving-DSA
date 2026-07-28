class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        i,j=0,len(nums)-1
        for k in range(len(nums)-1,-1,-1):
            a = nums[i]**2
            b = nums[j]**2
            if a>b:
                res[k]=a
                i+=1
            else:
                res[k]=b
                j-=1
        return res