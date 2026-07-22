class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        listt = [-1]*(len(nums2))
        for i in range(len(nums2)-1,-1,-1):
            if st:
                while st and st[-1]<nums2[i]:
                    st.pop()
                if st and st[-1]>nums2[i]:
                    listt[i]=st[-1]
            st.append(nums2[i])

        freq = {}
        for i in range(len(nums2)):
            freq[nums2[i]]=listt[i]

        res = []
        for item in nums1:
            res.append(freq[item])
        return res
    

