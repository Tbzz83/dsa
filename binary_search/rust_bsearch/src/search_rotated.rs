use crate::Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        println!("{:?}", nums);
        let mut l = 0;
        let mut r = nums.len()-1;

        while l <= r {
            let left = nums[l];
            let right = nums[r];
            let m = (l+r) / 2;
            let mid = nums[m];

            if mid == target {
                return m as i32;
            }

            if mid < left {
                if target < mid || target > right {
                    r = m;
                } else {
                    l = m+1;
                }
            } else if target > mid || target < left {
                l = m+1;
            } else {
                r = m;
            }
        }

        -1
    }
}
