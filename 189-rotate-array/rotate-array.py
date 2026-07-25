class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n
        i = n-k

        def rev(l,r):
            while l<=r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        rev(i,n-1)
        rev(0,i-1)
        rev(0,n-1)
        