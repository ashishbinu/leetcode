impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
        
        let mut l = -1;
        let mut r = nums.len() as i32;
        
        let condition = |i: usize| target <= nums[i];
        
        while r - l > 1 {
            let m = (l + r) / 2;
            
            if condition(m as usize) {
                r = m;
            }
            else {
                l = m;
            }
        }
        
        r
    }
}