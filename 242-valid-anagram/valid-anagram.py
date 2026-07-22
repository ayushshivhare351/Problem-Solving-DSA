class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        listt = list(set(s) | set(t))
        for item in listt:
            if (s.count(item)!=t.count(item)):
                return False
        return True