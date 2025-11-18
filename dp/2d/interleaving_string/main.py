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
        cache: dict[tuple[int, int], list[int]] = defaultdict(list)
        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        def dp(i1, i2, i3) -> int:
            if i1 == s1_len and i2 == s2_len and i3 == s3_len:
                return 0
            elif i1 == s1_len and i2 == s2_len and i3 < s3_len:
                return 1
            
            if (i1, i2) not in cache:
                cache[(i1, i2)] = [-1 for _ in range(s3_len + 1)]

            # -1 means non-initialized
            if cache[(i1, i2)][i3] == -1:
                if i1 in range(s1_len):
                    if s1[i1] == s3[i3]:
                        cache[(i1, i2)][i3] = dp(i1+1, i2, i3+1)
                    else:
                        cache[(i1, i2)][i3] = 1

                if cache[(i1, i2)][i3] != 0:
                    if i2 in range(s2_len):
                        if s2[i2] == s3[i3]:
                            cache[(i1, i2)][i3] = dp(i1, i2+1, i3+1)
                        else:
                            cache[(i1, i2)][i3] = 1

            return cache[(i1, i2)][i3]

        return dp(0,0,0) == 0

def main(): 
    s1 = "a"
    s2 = "b"
    s3 = "aba"
    sol = Solution()
    print(sol.isInterleave(s1, s2, s3))

if __name__ == "__main__":
    main()
