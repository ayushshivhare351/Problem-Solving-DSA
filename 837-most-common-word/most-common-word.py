class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        s = ""
        listt = []
        for item in paragraph:
            if item.isalpha():
                s += item
            else:
                listt.append(s)
                s = ""
        listt.append(s)

        freq = {}
        for item in listt:
            if item != "" and item not in banned:
                freq[item]=freq.get(item,0)+1
                
        maxf = max(freq.values())

        for item in freq:
            if freq[item]==maxf:
                return item

        