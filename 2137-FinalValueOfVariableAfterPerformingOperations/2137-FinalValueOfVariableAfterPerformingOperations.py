# Last updated: 8/16/2025, 7:33:54 AM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for x in operations:
            if "++" in x:
                res+=1
            if "--" in x:
                res-=1
        return res
        