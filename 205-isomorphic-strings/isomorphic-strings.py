class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq= {}
        for i in range(len(s)):
            if s[i] in freq and freq[s[i]]!=t[i]:
                return False
            freq[s[i]]=t[i]

        freq1= {}
        for i in range(len(t)):
            if t[i] in freq1 and freq1[t[i]]!=s[i]:
                return False
            freq1[t[i]]=s[i]

        return True
