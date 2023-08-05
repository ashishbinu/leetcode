impl Solution {
    
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        
        let rows = matrix.len();
        let cols = matrix[0].len();
        let n = (rows * cols) as i32;
        let mut l = -1;
        let mut r = n;
        
        let condition = |i: usize| target <= matrix[i / cols][i % cols];
        
        while r - l > 1 {
            let m = (l + r) / 2;
            
            if condition(m as usize) {
                r = m
            }
            else {
                l = m
            }
        }
        
        Some(target) == matrix.get(r as usize / cols).map(|col| *col.get(r as usize % cols).unwrap())
        
    }
}