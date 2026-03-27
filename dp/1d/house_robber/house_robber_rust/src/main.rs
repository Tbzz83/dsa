/*
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a straight line, i.e. the ith house is the neighbor of the (i-1)th and (i+1)th house.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.
*/

use std::{cmp::max, collections::HashMap};


struct Solution {}

impl Solution {
    pub fn rob(nums: Vec<i32>) -> i32 {
        let mut cache: HashMap<usize, i32> = HashMap::new();

        for (mut idx, num) in nums.iter().rev().enumerate() {
            idx = nums.len() - 1 - idx; // Get the index in reverse
            if idx == nums.len() - 1 {
                cache.insert(idx, *num);
                continue;
            } else if idx == nums.len() - 2 {
                cache.insert(idx, max(*num, *cache.get(&(idx+1)).unwrap()));
                continue;
            }

            let pick = *num + cache.get(&(idx+2)).unwrap();
            let skip = cache.get(&(idx+1)).unwrap();

            let max = max(&pick, &skip);
            cache.insert(idx, *max);
        }
        
        let res = cache.get(&0).unwrap();
        *res
    }
}

fn main() {
    dbg!(Solution::rob(vec![1,1,3,3]));
}
