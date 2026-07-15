class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        m = len(image)
        n = len(image[0])
        def recursion(r, c):
            if not (r >= 0 and c >= 0 and r < m and c < n):
                return image
            if image[r][c] == color or image[r][c] != start:
                return image
            image[r][c] = color
            
            recursion(r - 1, c)
            recursion(r + 1, c)
            recursion(r, c + 1)
            recursion(r, c - 1)
            return image
        return recursion(sr, sc)
