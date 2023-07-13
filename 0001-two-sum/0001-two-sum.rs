use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut mem: HashMap<i32,i32> = HashMap::new();
        for (k,&v) in nums.iter().enumerate(){
            if let Some(idx) = mem.get(&(target - v)) {
                return vec![*idx,k as i32];
            }
            mem.insert(v,k as i32);
        }
        vec![-1,-1]
    }
}