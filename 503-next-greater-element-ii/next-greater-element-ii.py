class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums+= nums
        n = len(nums)
        res = [-1]*(n)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if not st:
                res[i]=-1
            else:
                res[i]=nums[st[-1]]
            st.append(i)
        return res[:len(nums)//2]

