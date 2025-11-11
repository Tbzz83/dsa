use crate::common::Solution;

use std::collections::HashMap;

impl Solution {
    pub fn unique_paths(m: i32, n: i32) -> i32 {
        let mut memo: HashMap<(i32,i32), i32> = HashMap::new();

        fn dp(m: i32, n: i32,target_m: i32, target_n: i32, memo: &mut HashMap<(i32, i32), i32>) -> i32 {
            if m == target_m && n == target_n {
                memo.insert((m,n), 0);
                return 0
            }
            if m >= target_m || n >= target_n {
                return 0
            }

            if let Some(ways) = memo.get(&(m,n)) {
                return *ways;
            }

            let first = dp(m+1,n,target_m, target_n, memo);

            let second = dp(m,n+1,target_m, target_n, memo);

            memo.insert((m,n),
                1 + first + second
            );

            *memo.get(&(m,n)).unwrap()
        }

        1 + dp(0,0,m-1,n-1,&mut memo)
    }
}
