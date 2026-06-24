'''
You are given a string s which contains only three types of characters: '(', ')' and '*'.

Return true if s is valid, otherwise return false.

A string is valid if it follows all of the following rules:

    Every left parenthesis '(' must have a corresponding right parenthesis ')'.
    Every right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    A '*' could be treated as a right parenthesis ')' character or a left parenthesis '(' character, or as an empty string "".
'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        res = false
        def dfs(i: int, stack: list[str]):
            nonlocal res

            if i >= len(s):
                if stack:
                    res = False
                else:
                    res = True
                return
            
            char = s[i]

            if char == ")":
                if not stack: 
                    res = False
                    return 
                stack.pop()

            elif char == "(":
                stack.append(char)

            else:
                # pop
                if stack:
                    popped = stack.pop()
                    if dfs(i+1, stack):
                        return True
                    stack.append(popped)

            # includes the skip case of *
            return dfs(i+1, stack)

        return res
        
s = "((**)"

sol = Solution()

print(sol.checkValidString(s))
