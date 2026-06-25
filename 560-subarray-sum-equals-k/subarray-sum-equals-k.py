class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dictt = {0:1}
        summ = 0
        res = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ-k in dictt:
                res += dictt[summ-k]
            dictt[summ]=dictt.get(summ,0)+1
        return res