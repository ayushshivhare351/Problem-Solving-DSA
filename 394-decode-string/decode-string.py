class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        nt = []
        num = 0
        for item in s:
            if item.isdigit():
                num = (num*10)+int(item)
            elif item == '[':
                nt.append(num)
                num = 0
                st.append('[')
            elif item == ']':
                res = ''
                while st and st[-1]!='[':
                    res =  st.pop() + res
                st.pop()
        
                st.append(res*nt.pop())
            else:
                st.append(item)
        ans = ''
        while st:    
            ans = st.pop() + ans

        return ans









