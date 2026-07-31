class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res= [0]*len(nums)
        i,j = 0,n-1
        k = n-1
        while k>=0:
            a =nums[i]*nums[i]
            b = nums[j]*nums[j]
            if a >b :
                res[k] =a
                i+=1
            else:
                res[k]=b
                j-=1
            k-=1
        return res




