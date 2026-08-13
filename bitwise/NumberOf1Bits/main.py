class Solution:
    # Easy solution
    def hammingWeight(self, n: int) -> int:
        t = 0
        while n > 0:
            if n & 1 == 1:
                t += 1
            n = n >> 1

        return t

    # Good luck coming up with this yourself
    def hammingWeightOptimal(self, n: int) -> int:
        t = 0
        op = 1
        while n > 0:
            print(n)
            op = n & (n-1)
            t += 1
            n = op

        return t

sol = Solution()
n = 10
print(sol.hammingWeightOptimal(n))
