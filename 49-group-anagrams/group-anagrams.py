class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        dictt = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in dictt:
                dictt[key].append(s)
            else:
                dictt[key]=[s]
        return list(dictt.values())