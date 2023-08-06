impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut l = 0;
        let mut r = *piles.iter().max().unwrap();
        
        let f = |k| {
            let mut hrs = 0;
            for v in &piles {
                hrs += (*v - 1)/k + 1; // ceil (v/k) = (v + k -1) /k
                if hrs > h {
                    return false;
                }
            }
            return true;
        };
        
        while r -l > 1 {
            let m = l + (r - l) / 2;
            if f(m) {
                r = m;
            } else {
                l = m;
            }
        }
        
        r
    }
}
