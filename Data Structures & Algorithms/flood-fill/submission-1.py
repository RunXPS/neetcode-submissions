class Solution:

    def helper(self, image: List[List[int]], sr: int, sc: int, color: int, starting) -> None:
        # set current px color
        image[sr][sc] = color

        if sr - 1 >= 0 and image[sr - 1][sc] == starting:
            self.helper(image, sr - 1, sc, color, starting)
        
        if sr + 1 < len(image) and image[sr + 1][sc] == starting:
            self.helper(image, sr + 1, sc, color, starting)
        
        if sc - 1 >= 0 and image[sr][sc - 1] == starting:
            self.helper(image, sr, sc - 1, color, starting)
        
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == starting:
            self.helper(image, sr, sc + 1, color, starting)


    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting = image[sr][sc]
        if starting != color:
            self.helper(image, sr, sc, color, starting)
        return image