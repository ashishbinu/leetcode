impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut l = 0;
        let mut r = *piles.iter().max().unwrap();
        
        let f = |k| {
            let hrs = piles.iter().fold(0i64, |acc, v| acc + (*v as i64 - 1) / k as i64 + 1);
            hrs <= h as i64
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
