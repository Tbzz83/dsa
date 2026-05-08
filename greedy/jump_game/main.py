'''
You are given an integer array nums where each element nums[i] indicates your maximum jump length at that position.

Return true if you can reach the last index starting from index 0, or false otherwise.


ex. 1. 
[1,2,1,0,1]

starting at 1, I have to jump 1. 

starting at 2, I have a choice:
    jump 1
        starting at 1, jump one:
            0. End

    jump 2
        start at 0. End

return False


ex. 2.
[1,2,0,1,0]

starting at 1, jump 1
    starting at 2:
        jump 2:
            start at 1:
                jump 1:
                    finished!

        jump 1:
            don't evaluate

ex. 3. 
[999900,1mil,0,3,10,..0,100000,0,0....] let n = 1 million


iterate backward.
goal is to find value that can reach the 1 millionth idx

find value that can.

goal is to find value that can reach 1 million - valueth idx

find value that can. 

at 0th idx, if that value can reach the current target, return True else False

if 0th idx == 0 return False
'''

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) == 0 or (nums[0] == 0 and len(nums) > 1):
            return False

        target_idx = len(nums) - 1
        for idx in range(len(nums)-1, -1, -1):
            num = nums[idx]
            max_idx_can_reach = num + idx

            if max_idx_can_reach >= target_idx:
                target_idx = idx
        
        return target_idx == 0

def main():
    sol = Solution()
    print(sol.canJump([1,2,1,0,1]))

if __name__ == "__main__":
    main()
