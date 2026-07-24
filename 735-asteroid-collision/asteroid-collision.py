class Solution:
    def asteroidCollision(self, nums: List[int]) -> List[int]:
        if len(nums)==1 or len(nums)==0:
            return nums
        st = []
        for item in nums:
            st.append(item)
            while len(st)>1 and st[-1]<0 and st[-2]>0:
                    b = st.pop()
                    a = st.pop()
                    if abs(a)==abs(b):
                        continue
                    elif abs(a)>abs(b):
                        st.append(a)
                    else:
                        st.append(b)
        return st
            