# Last updated: 8/20/2025, 11:21:24 PM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        res = Counter(words[0])

        for x in words:
            res &= Counter(x)
        
        return list(res.elements())