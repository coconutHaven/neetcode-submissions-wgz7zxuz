class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        def recursion(image, sr, sc, color, start):
            m = len(image)
            n = len(image[0])

            if not (sr >= 0 and sc >= 0 and sr < m and sc < n):
                return image
            if image[sr][sc] == color or image[sr][sc] != start:
                return image
            if image[sr][sc] == start:
                image[sr][sc] = color
            
            image = recursion(image, sr - 1, sc, color, start)
            image = recursion(image, sr + 1, sc, color, start)
            image = recursion(image, sr, sc + 1, color, start)
            image = recursion(image, sr, sc - 1, color, start)
            return image
        return recursion(image, sr, sc, color, start)
