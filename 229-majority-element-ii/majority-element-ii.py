class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority1 = None
        majority2 = None
        count1 = 0
        count2 = 0
        for i in range(len(nums)):
            if nums[i]==majority1:
                count1+=1
            elif nums[i]==majority2:
                count2+=1
            elif count1==0:
                majority1 = nums[i]
                count1 = 1
            elif count2==0:
                majority2  = nums[i]
                count2 = 1    
            else:
                count1-=1
                count2-=1
        
        res = []
        if nums.count(majority1) > len(nums)/3:
            res.append(majority1)
        if nums.count(majority2) > len(nums)/3:
            res.append(majority2)

        return res