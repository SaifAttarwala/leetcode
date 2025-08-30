# Last updated: 8/30/2025, 6:52:25 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for x in words:
            if set(x).issubset(set(allowed)):
                res += 1
        return res
        