impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        
        let m = matrix.len();
        let n = matrix[0].len();
        
        let mut rx = (n - 1);
        let mut ry = 0;
        
        while rx < n && ry < m {
            if matrix[ry][rx] > target {
                rx -= 1;
            }
            else if matrix[ry][rx] < target {
                ry += 1;
            }
            else {
                return true;
            }
        }
        
        return false;
    }
}