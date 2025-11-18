# You are given three strings s1, s2, and s3. Return true if s3 is formed by interleaving s1 and s2 together or false otherwise.
# 
# Interleaving two strings s and t is done by dividing s and t into n and m substrings respectively, where the following conditions are met
# 
#     |n - m| <= 1, i.e. the difference between the number of substrings of s and t is at most 1.
#     s = s1 + s2 + ... + sn
#     t = t1 + t2 + ... + tm
#     Interleaving s and t is s1 + t1 + s2 + t2 + ... or t1 + s1 + t2 + s2 + ...
# 
# You may assume that s1, s2 and s3 consist of lowercase English letters.
#
# Can only use char from s1 or s2 at most ONCE
#
# Have to use all chars from both s1 and s2

from collections import defaultdict
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache: dict[tuple[int, int], bool] = {}
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        if s1_len + s2_len != s3_len:
            return False

        def dp(i1, i2) -> bool:
            if i1 == s1_len and i2 == s2_len:
                return True
            
            if (i1, i2) not in cache:
                ok = False

                if i1 < s1_len and s1[i1] == s3[i1+i2]:
                    ok = dp(i1+1, i2)

                if i2 < s2_len and s2[i2] == s3[i1+i2] and not ok:
                    ok = dp(i1, i2+1)

                cache[(i1, i2)] = ok

            return cache[(i1, i2)]

        return dp(0,0)

def main(): 
    s1 = "ab"
    s2 = "ac"
    s3 = "aabc"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))

if __name__ == "__main__":
    main()
