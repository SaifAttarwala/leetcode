# Last updated: 8/18/2025, 4:02:15 AM
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dic = Counter(arr)
        dic = dic.most_common(1)
        return dic[0][0]