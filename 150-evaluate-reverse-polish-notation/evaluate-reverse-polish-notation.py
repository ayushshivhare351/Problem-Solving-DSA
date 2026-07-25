class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for item in tokens:
            if item not in "+-*/":
                st.append(int(item))
            elif item == '+':
                a = st.pop()
                b = st.pop()
                st.append(b+a)
            elif item == '-':
                a = st.pop()
                b = st.pop()
                st.append(b-a)
            elif item == '*':
                a = st.pop()
                b = st.pop()
                st.append(b*a)
            elif item == '/':
                a = st.pop()
                b = st.pop()
                st.append(int(b/a))
        return st[-1]