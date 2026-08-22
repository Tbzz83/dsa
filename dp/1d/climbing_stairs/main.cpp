/*
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

*/

#include <iostream>
#include <functional>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        unordered_map<int, int> memo;

        function<int(int)> dp = [&](int step) {
            // Write min number of base cases to avoid going out of bounds
            if (step == n) {
                return 0;
            } else if (step == n - 1) {
                return 1;
            } else if (step == n - 2) {
                return 2;
            }

            // If step not in memo
            if (memo.find(step) == memo.end()) {
                memo[step] = dp(step+1) + dp(step+2);
            }

            return memo[step];
        };

        auto res = dp(0);
        return res;
    }
};

int main() {
    auto sol = Solution();
    auto res = sol.climbStairs(3);
    cout << res << "\n";
}
