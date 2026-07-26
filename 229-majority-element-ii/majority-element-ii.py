class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        m1 = None
        m2 = None
        c1 = 0
        c2 = 0
        for i in range(len(nums)):
            if nums[i]==m1:
                c1+=1
            elif nums[i]==m2:
                c2+=1
            elif c1==0:
                m1= nums[i]
                c1 = 1
            elif c2==0:
                m2 = nums[i]
                c2 = 1
            else:
                c1-=1
                c2-=1
        
        res = []
        if nums.count(m1)>(len(nums)//3):
            res.append(m1)
        if nums.count(m2)>(len(nums)//3):
            res.append(m2)
        return res