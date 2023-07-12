use std::collections::*;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut mem: HashSet<i32> = HashSet::with_capacity(nums.len());
        for num in nums {
            if !mem.insert(num) {
                return true;
            }
        }
        false
    }
}