class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*(n)
        st = []
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<=nums[i]:
                st.pop()
            if not st:
                res[i]=0
            else:
                res[i]=st[-1]-i
            st.append(i)
        return res
