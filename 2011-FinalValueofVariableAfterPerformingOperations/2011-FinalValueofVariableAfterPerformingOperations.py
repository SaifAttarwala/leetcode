# Last updated: 8/15/2025, 8:57:52 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for x in operations:
            if "++" in x:
                res+=1
            if "--" in x:
                res-=1
        return res
        