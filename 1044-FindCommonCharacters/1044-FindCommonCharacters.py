# Last updated: 8/24/2025, 11:55:17 PM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = Counter(words[0])

        for x in words:
            res &= Counter(x)
        
        return list(res.elements())