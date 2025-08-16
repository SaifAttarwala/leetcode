# Last updated: 8/16/2025, 7:33:51 AM
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        res = 0
        for i in hours:
            if i >= target:
                res += 1
        return res