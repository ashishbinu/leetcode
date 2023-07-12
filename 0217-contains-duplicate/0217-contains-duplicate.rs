use std::collections::*;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut mem: HashSet<i32> = HashSet::new();
        for num in nums {
            if mem.contains(&num) {
                return true;
            }
            mem.insert(num);
        }
        return false;
    }
}