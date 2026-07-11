class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []
        def solve(i):
            if i>= len(nums):
                if not temp.copy() in res:
                    res.append(temp.copy())
                    return
            temp.append(nums[i])
            solve(i+1)
            temp.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            solve(i+1)
        solve(0)
        return res