# Last updated: 7/22/2025, 1:05:40 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        string1 = min(strs)
        string2 = max(strs)

        for i, char in enumerate(string1):
            if string2[i] != char:
                return string1[:i]
        return string1

        


            

        