class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        ss = ""
        listt = []
        for item in s.lower():
            if item.isalpha():
                ss+=item
            else:
                if ss:
                    listt.append(ss)
                    ss = ""
        
        if ss:
            listt.append(ss)

        freq =  {}
        for item in listt:
            if item not in banned:
                freq[item]=freq.get(item,0)+1
        maxf = max(freq.values())
        for item in freq:
            if freq[item]==maxf:
                return item