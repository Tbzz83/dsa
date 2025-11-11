/*
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Tuples ARE hashable in rust (so long as constituent elements implement hash)

store for each coord (m,n) how many ways are there to reach the end.

For example, the target element coords (m-1, n-1) should store 0, since you're at
the end, there are no more ways to reach the end. The square directly above has 1 way, same
with the square directly to the left

We can only go down and right, so no need to worry about accidentally retracing steps.
*/

mod unique_paths;
mod common;
mod longest_common_subsequence;

use crate::common::Solution;

fn main() {
    let m = 3;
    let n = 3;
    println!("Unique paths for grid of size '{m}', '{n}' : {}", Solution::unique_paths(3, 3));

    let a = String::from("abcde");
    let b = String::from("ace");
    println!("Length of longest common subseq between '{a}' and '{b}' {}", Solution::longest_common_subsequence(String::from(a.clone()), String::from(b.clone())));
}
