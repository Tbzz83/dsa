'''
You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i. For example, if you are at nums[i], you can jump to any index i + j where:

    j <= nums[i]
    i + j < nums.length

You are initially positioned at nums[0].

Return the minimum number of jumps to reach the last position in the array (index nums.length - 1). You may assume there is always a valid answer.

Iterate backwards:

[2,4,1,1,1]

starting at 1 (end), 

at end:

cache[idx, min_to_reach_end]

{
    4: 0,
}

starting at 1 (3rd idx), 

jump max avail (1). look up cache for that value: 0

{
    4: 0,
    3: 1 + cache[i+1] = 1,
}

...

{
    4: 0, 
    3: 1,
    2: 2,
}

starting at 4 (1st idx), jump max avail (4):
look up min to complete for that value (0):
{
    4: 0,
    3: 1,
    2: 2,
    1: 1,
    0: 2
}

Question?

Is it possible that when we do a max jump and see that cache has a value that isn't -1, do we
need to look at the other values we could have jumped? Yes



'''

class Solution:
    def jump(self, nums: list[int]) -> int:
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            farthest_i_reachable = 0

            # Iterate through indices in current window
            for i in range(l,r+1):
                jump_distance_for_i = nums[i]
                farthest_i_reachable = max(farthest_i_reachable, i + jump_distance_for_i)

            l = r + 1
            r = farthest_i_reachable
            res += 1

        return res

    def jump_suboptimal(self, nums: list[int]) -> int:
        # -1 val means can't complete
        cache: dict[int, int] = {}

        for idx in range(len(nums)-1,-1,-1):
            num = nums[idx]
            if idx == len(nums)-1:
                cache[idx] = 0
                continue

            min_to_complete_for_idx = (False, float('inf'))
            # Iterate from max jump can make to min
            for jump in range(num, 0, -1):
                if jump + idx >= len(nums)-1:
                    min_to_complete_for_idx = (True, 1)
                    break

                # Is the jump we can make completable?
                if cache[jump+idx] >= 0:
                    min_completions = min(min_to_complete_for_idx[1], cache[jump+idx]+1)
                    min_to_complete_for_idx = (True, min_completions)
                    print(idx, min_to_complete_for_idx)

            if min_to_complete_for_idx[0]:
                cache[idx] = min_to_complete_for_idx[1]
            else:
                cache[idx] = -1

        print(cache)
        return cache[0]

def main():
    sol = Solution()
    #print(sol.jump([1,2,1,0,1]))
    print(sol.jump([3,6,0,3,0,1,1,0]))
    print(sol.jump([2,4,1,1,1,1]))
    print(sol.jump([2,1,2,1,0]))

if __name__ == "__main__":
    main()
