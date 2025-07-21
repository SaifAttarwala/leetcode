# Last updated: 7/22/2025, 1:05:34 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = map(str,digits)
        num = int("".join(num)) + 1 
        
        res = []
        
        for i in str(num):
            res.append(int(i))
        return res
        