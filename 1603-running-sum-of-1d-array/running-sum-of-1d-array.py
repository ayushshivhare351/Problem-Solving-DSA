class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        n = len(nums)
        summ = 0
        for i in range(n):
            summ+=nums[i]
            prefix.append(summ)
        return prefix