class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt = {}



        for i in range(len(nums)):
            summ = target-nums[i]
            if summ in dictt:
                return [dictt[summ],i]
            else:
                dictt[nums[i]]= i
    

         