class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        def solve(i,summ,temp):
            if summ==target:
                res.append(temp.copy())
                return

            if summ>target:
                return

            if i>= n:
                return
                
            temp.append(nums[i])
            #solve(i+1,summ+nums[i],temp)

            solve(i,summ+nums[i],temp)

            
            temp.pop()
            solve(i+1,summ,temp)
            
        solve(0,0,[])   
        return res