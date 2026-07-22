class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        for item in "thequickbrownfoxjumpsoverthelazydog":
            if item not in sentence:
                return False
        return True