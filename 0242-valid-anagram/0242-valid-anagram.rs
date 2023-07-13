impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut counter = [0; 26];
        
        let s = s.bytes();
        let t = t.bytes();
        
        s.for_each(|c| {counter[c as usize- 'a' as usize] += 1;});
        t.for_each(|c| {counter[c as usize- 'a' as usize] -= 1;});
        
        counter.iter().all(|&i| i == 0 )
    }
}