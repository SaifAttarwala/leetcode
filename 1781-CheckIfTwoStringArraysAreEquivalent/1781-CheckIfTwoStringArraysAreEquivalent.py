# Last updated: 8/16/2025, 7:33:59 AM
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        if "".join(word1) == "".join(word2):
            return True
        return False
        