class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int,initial_color=None) -> List[List[int]]:
        
        if initial_color is None:
            initial_color = image[sr][sc]
        
        nr = len(image) - 1
        nc = len(image[0]) - 1
        if sr < 0 or sc < 0 or sr > nr or sc > nc or image[sr][sc] != initial_color or image[sr][sc]==color: return image
        
        image[sr][sc] = color
        
        self.floodFill(image,sr-1,sc,color,initial_color)
        self.floodFill(image,sr+1,sc,color,initial_color)
        self.floodFill(image,sr,sc-1,color,initial_color)
        self.floodFill(image,sr,sc+1,color,initial_color)
        
        return image
        