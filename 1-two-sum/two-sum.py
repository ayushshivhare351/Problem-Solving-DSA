class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums )
        freq = {}
        for j in range(n):
            if target-nums[j] in freq:
                return [freq[target-nums[j]],j]
            freq[nums[j]]=j
            