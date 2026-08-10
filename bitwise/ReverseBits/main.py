'''
https://neetcode.io/problems/reverse-bits/question?list=neetcode150


Given a 32-bit unsigned integer n, reverse the bits of the binary representation of n and return the result.

Explanation: Reversing 00000000000000000000000000010101, which represents the unsigned integer 21, 
gives us 10101000000000000000000000000000 which represents the unsigned integer 2818572288.


011
110

01
10
'''


class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | bit << (31 - i)
            # NOTE
            # res += bit << (31 - i) also works because in binary:
            # 4 + 1 == 5
            # 100 + 001 == 101
            # 5 + 2 == 7
            # 101 + 010 == 111
        return res

sol = Solution()

print(1|4)

n = int("00000000000000000000000000010101", 2)

print(sol.reverseBits(n))
