from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i) -> int:
            if i >= len(s):
                return 1
            elif s[i] == "0":
                return 0

            opt_1 = 0
            if i + 2 <= len(s):
                slice = s[i:i+2]

                # valid
                if int(slice) <= 26:
                    opt_1 = dp(i+2)
                    print(opt_1, i)

            opt_2 = dp(i+1)
            return opt_1 + opt_2
        return dp(0)
                
        
sol = Solution()

print(sol.numDecodings("27"))
