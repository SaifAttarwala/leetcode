# Last updated: 8/6/2025, 10:08:52 PM
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(s)
        
        for i, val in enumerate(s):
            res[indices[i]] = val

        return "".join(res)

