impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        
        let n = nums.len() as i32;
        let mut l = -1;
        let mut r = n;
        
        let condition = |i|  {
            let first = nums[0];
            let last = nums[(n-1) as usize];
            
            if target <= last {
                target <= nums[i] && nums[i] <= last
            }
            else {
                target <= nums[i] || nums[i] <= last
            }
        };
        
        while r-l > 1 {
            let m = (l + r) / 2;
            
            if condition(m as usize) {
                r = m
            }
            else {
                l = m
            }
        }
        
        if r == n || nums[r as usize] != target {
            return -1;
        }
        r
        
    }
}