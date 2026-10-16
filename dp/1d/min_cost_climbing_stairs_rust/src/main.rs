/*
https://neetcode.io/problems/min-cost-climbing-stairs/question?list=neetcode150
You are given an array of integers cost where cost[i] is the cost of taking a step from the ith floor of a staircase. After paying the cost, you can step to either the (i + 1)th floor or the (i + 2)th floor.

You may choose to start at the index 0 or the index 1 floor.

Return the minimum cost to reach the top of the staircase, i.e. just past the last index in cost.
*/

use std::cmp::min;

struct Solution {}

impl Solution {
    pub fn min_cost_climbing_stairs(cost: Vec<i32>) -> i32 {
        let len = cost.len();
        if len == 1 {
            return cost[0];
        }

        let mut a = cost[len-1];
        let mut b = cost[len-2];

        for i in (0..(len-2)).rev() {
            let item = cost[i];
            let tmp = b;
            b = min(a,b) + item;
            a = tmp;
        }

        min(a,b)
    }
}

pub fn main() {
    let mut cost = vec![1,2,3];
    //cost = vec![10,9,8,7,6,5];

    println!("{}", Solution::min_cost_climbing_stairs(cost));
}
