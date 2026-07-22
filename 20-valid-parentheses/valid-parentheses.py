class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] in '({[':
                st.append(s[i])
            else:
                if not st:
                    return False
                top = st.pop()
                if s[i]==')' and top!='(':
                    return False
                elif s[i]=='}' and top!='{':
                    return False
                elif s[i]==']' and top!='[':
                    return False
        if st:
            return False
        return True