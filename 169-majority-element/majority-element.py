class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i]==majority:
                count+=1
            elif nums[i]!=majority:
                count-=1
                if count==0:
                    count = 1
                    majority = nums[i]
        if nums.count(majority) > len(nums)/2:
            return majority

