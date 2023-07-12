impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len() {
            return false;
        }
        let mut counter: [i32; 26] = [0; 26];
        
        for (a,b) in s.bytes().zip(t.bytes()) {
            counter[(a - 'a' as u8) as usize] += 1;
            counter[(b - 'a' as u8) as usize] -= 1;
        }
        
        for i in counter {
            if i != 0 {
                return false;
            }
        }
        return true;
    }
}