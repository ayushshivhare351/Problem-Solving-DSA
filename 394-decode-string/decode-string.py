class Solution:
    def decodeString(self, s: str) -> str:
        n = []
        st = []
        x = 0
        for item in s:
            if item.isdigit():
                x = x*10 + int(item)
            elif item=='[':
                n.append(x)
                x = 0
                st.append('[')
            elif item==']':
                string = ""
                while st[-1]!='[':
                    string = st.pop() + string
                st.pop()
                number = n.pop()
                st.append(string*int(number))
            else:
                st.append(item)
   
        return "".join(st)