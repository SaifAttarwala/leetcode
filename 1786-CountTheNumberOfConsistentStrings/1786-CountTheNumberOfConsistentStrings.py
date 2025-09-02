# Last updated: 03/09/2025, 02:52:53
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for x in words:
            if set(x).issubset(set(allowed)):
                res += 1
        return res
        