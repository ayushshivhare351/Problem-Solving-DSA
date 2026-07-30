class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        maxi = 1
        for i in range(len(s)):
            sett = set()
            sett.add(s[i])
            count = 1
            for j in range(i+1,len(s)):
                if s[j] not in sett:
                    sett.add(s[j])
                    count +=1
                    maxi = max(maxi,count)
                else:
                    break
        return maxi