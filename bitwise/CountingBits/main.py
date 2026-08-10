'''
https://neetcode.io/problems/counting-bits/question?list=neetcode150
Given an integer n, count the number of 1's in the binary representation of every number in the range [0, n].

Return an array output where output[i] is the number of 1's in the binary representation of i.
'''

class Solution:
    # Good luck coming up with this yourself
    def hammingWeightOptimal(self, n: int) -> int:
        t = 0
        op = 1
        while n > 0:
            op = n & (n-1)
            t += 1
            n = op

        return t

    def countBits(self, n: int) -> list[int]:
        res = []
        for i in range(n+1):
            res.append(self.hammingWeightOptimal(i))
        return res
sol = Solution()
print(sol.countBits(4))
