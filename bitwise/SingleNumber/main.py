def single_number(nums: list[int]) -> int:
    res = 0
    for num in nums:
        res ^= num
    return res

def main():
    res = 0
    nums = [1,1,2,2,3]

if __name__ == "__main__":
    main()
