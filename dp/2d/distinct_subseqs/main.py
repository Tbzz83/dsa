# You are given two strings s and t, both consisting of english letters.
# 
# Return the number of distinct subsequences of s which are equal to t.
# 
# Example 1:
# 
# Input: s = "caaat", t = "cat"
# 
# Output: 3
# 
# Explanation: There are 3 ways you can generate "cat" from s.
# 
#     (c)aa(at)
#     (c)a(a)a(t)
#     (ca)aa(t)
# 


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        cache: dict[tuple[int, int], int] = {}

        s_len, t_len = len(s), len(t)

        def dp(si, ti) -> int:
            if ti >= t_len:
                return 1
            elif si >= s_len:
                return 0

            key = (si,ti)
            if key in cache:
                return cache[key]

            pick = 0
            if s[si] == t[ti]:
                pick = dp(si+1, ti+1)

            skip = dp(si+1, ti)

            cache[key] = pick+skip

            return cache[key]

        return dp(0,0)
            

def main():
    sol = Solution()
    print(sol.numDistinct("caaat", "cat"))

if __name__ == "__main__":
    main()
