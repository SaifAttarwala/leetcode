# Last updated: 8/18/2025, 4:02:11 AM
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dictionary = Counter(nums).most_common()
        
        res = []
        dictionary.sort(key = lambda x: x[0], reverse = True)
        dictionary.sort(key = lambda x: x[1])

        for x in dictionary:
            a,b = x
            res.extend([a]*b)

        return res

        