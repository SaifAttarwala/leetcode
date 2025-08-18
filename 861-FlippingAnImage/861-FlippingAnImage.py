# Last updated: 8/19/2025, 4:08:04 AM
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        image = [x[::-1] for x in image]

        image = [[1 if x == 0 else 0 for x in row] for row in image]

        return image
        