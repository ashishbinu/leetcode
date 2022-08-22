class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def floodfill(row,col):
            if row < 0 or row >= row_len: return
            if col < 0 or col >= col_len: return
            if image[row][col] != icolor: return
            
            if image[row][col] == fcolor: return image

            image[row][col] = color

            floodfill(row-1, col)
            floodfill(row+1, col)
            floodfill(row, col-1)
            floodfill(row, col+1)

            return image
        
        icolor = image[sr][sc]
        fcolor = color
        row_len = len(image)
        col_len = len(image[0])
        return floodfill(sr,sc)
        
        
        