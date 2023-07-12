use std::collections::*;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        nums.len() != nums.into_iter().collect::<HashSet<i32>>().len()
    }
}