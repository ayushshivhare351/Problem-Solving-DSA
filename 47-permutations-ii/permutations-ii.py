class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []
        nums.sort()
        st = set()
        def solve(nums,temp):
            if len(temp)==len(nums):
                if temp.copy() not in res:
                    res.append(temp.copy())
                    return
            for i in range(len(nums)):
                if i not in st:
   
                    if i>0 and nums[i]==nums[i-1] and i-1 not in st:
                        continue
                        
                    temp.append(nums[i])
                    st.add(i)
                
                    solve(nums,temp)
                
                    temp.pop()
                    st.remove(i)
                
            
        
        solve(nums,temp)
        return res
                
