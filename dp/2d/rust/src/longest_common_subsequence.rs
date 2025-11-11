use crate::common::Solution;

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let mut memo: Vec<Vec<i32>> = vec![];
        for i in 0..(text1.len()+1) {
            memo.push(vec![]);
            for _ in 0..(text2.len()+1) {
                memo[i].push(-1);
            }
        }

        fn dp(i: usize, j: usize, max_i: usize, max_j: usize, text1: &[u8], text2: &[u8], memo: &mut Vec<Vec<i32>>) -> i32 {
            if i >= max_i || j >= max_j {
                return 0;
            }

            if memo[i][j] != -1 {
                return memo[i][j];
            }

            if text1[i] == text2[j] {
                memo[i][j] = 1 + dp(i+1, j+1, max_i, max_j, text1, text2, memo);
            } else {
                memo[i][j] = std::cmp::max(
                    dp(i+1, j, max_i, max_j, text1, text2, memo),
                    dp(i, j+1, max_i, max_j, text1, text2, memo),
                )
            }

            memo[i][j]
        }

        dp(0,0,text1.len(), text2.len(), text1.as_bytes(), text2.as_bytes(), &mut memo)
    }
}
