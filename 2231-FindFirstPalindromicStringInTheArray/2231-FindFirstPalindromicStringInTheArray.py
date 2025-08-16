# Last updated: 8/16/2025, 7:33:53 AM
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for x in words:
            if x == x[::-1]:
                return x
        return ""