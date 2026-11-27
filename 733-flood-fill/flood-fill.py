class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        og = image[sr][sc]
        if color==og:
            return image
        n = len(image)
        m = len(image[0])
        def fun(i,j):
            if i<0 or j<0 or i>=n or j>=m or image[i][j]!=og:
                return
            image[i][j]=color 
            fun(i+1,j)
            fun(i-1,j)
            fun(i,j+1)
            fun(i,j-1)
        fun(sr,sc)
        return image