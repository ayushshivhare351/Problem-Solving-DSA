class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        summ = 0
        for i in range(0,n,2):
            summ += nums[i]
        return summ