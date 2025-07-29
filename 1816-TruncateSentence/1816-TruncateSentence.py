# Last updated: 7/29/2025, 6:46:30 PM
class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split(" ")
        s = s[:k]
        return " ".join(s)
        