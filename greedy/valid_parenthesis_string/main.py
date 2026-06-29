'''
You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

    Every left parenthesis '(' must have a corresponding right parenthesis ')'.
    Every right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".


SOLUTION:

Okay so this is a pretty hard problem, honestly I think it should be a hard and not a medium but what do I know. 

So you can actually solve this using backtracking -> DP (2D memoization). 

The greedy solution is way less intuitive.

You store a left_min and a left_max. Each time you encounter a wild `*`, you decrement the left_min and increment the left_max.
The brute force way you assume that you have to compute all three decisions per unique state, but in this case you don't. 

The TRICK is that at the end you will have some left_min, and some left_max values, and you know whether the string is valid
if `0` falls within the range between left_min and left_max: `return 0 in range(left_min, left_max)`

This is clever as you basically ignore all the substates that you would have had to manually compute before, because you assume that 
even with all those decisions you can never have more lefts than the left_max, or less lefts than the left_min. pretty darn clever.
Since you always increment or decrement by one, you can also assume that all the states between left_min < left_max exist.
'''

class Solution:
    def checkValidStringDp(self, s: str) -> bool:
        memo = {}

        def dp(i: int, lefts: int) -> bool:
            # base case
            if i >= len(s):
                return lefts == 0
            elif lefts < 0:
                return False

            key = (i,lefts)

            if key not in memo:

                match s[i]:
                    case "(":
                        memo[key] = dp(i+1, lefts + 1)
                    case "*":
                        a = dp(i+1, lefts + 1)
                        if not a:
                            b = dp(i+1, lefts - 1)
                            if not b:
                                memo[key] = dp(i+1, lefts)
                            else:
                                memo[key] = b
                        else:
                            memo[key] = a
                    case ")":
                        memo[key] = dp(i+1, lefts - 1)

            else:
                print("CACHE HIT")

            return memo[key]

        res = dp(0,0)
        print(memo)
        return res

    def checkValidStringBacktrack(self, s: str) -> bool:
        res = False

        def backtrack(i: int, lefts: int):
            nonlocal res
            if res:
                return 
            if i >= len(s):
                if not res:
                    res = lefts == 0
                return 
            if lefts < 0:
                return

            match s[i]:
                case "(":
                    backtrack(i+1, lefts + 1)
                case "*":
                    backtrack(i+1, lefts + 1)
                    backtrack(i+1, lefts - 1)
                    backtrack(i+1, lefts)

                case ")":
                    backtrack(i+1, lefts - 1)

        backtrack(0, 0)
        return res


    def checkValidString(self, s: str) -> bool:

        left_min = left_max = 0

        for char in s:
            match char:
                case "(":
                    left_min += 1
                    left_max += 1
                case "*":
                    if left_min > 0:
                        left_min -= 1
                    left_max += 1
                case ")":
                    if left_max == 0:
                        return False
                    if left_min > 0:
                        left_min -= 1
                    left_max -= 1

        return 0 in range(left_min, left_max+1)
        
        
s="(()(*))"
s = "((*))"
s="((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

sol = Solution()

print(sol.checkValidStringDp(s))
