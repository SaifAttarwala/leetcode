# Last updated: 8/16/2025, 7:34:01 AM
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        
        for i, val in enumerate(s):
            res[indices[i]] = val

        return "".join(res)

