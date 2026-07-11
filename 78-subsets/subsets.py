class Solution:   
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subsett = []
        def solve(i):
            if i>= len(nums):
                res.append(subsett.copy())
                return
            #take
            subsett.append(nums[i])
            solve(i+1)
            #skip
            subsett.pop()
            solve(i+1) 
            
        solve(0)
        return res