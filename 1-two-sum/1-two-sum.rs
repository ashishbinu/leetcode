use std::collections::HashMap;
        
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut mem: HashMap<i32,i32> = HashMap::new();
        
        for (idx,&val) in nums.iter().enumerate() {
            let v = target - val; 
            if mem.contains_key(&v) {
                return vec![*mem.get(&v).unwrap(),idx as i32];
            }
            mem.insert(val,idx as i32);
        }
        return vec![];
    }
}