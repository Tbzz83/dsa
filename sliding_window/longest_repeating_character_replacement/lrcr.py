from collections import defaultdict
def characterReplacement(s: str, k: int) -> int:
    if len(s) == 0:
        return 0

    counts: dict[str, int] = defaultdict(int)

    swaps_used: int = 0
    res: int = 0

    l = r = 0

    while r < len(s):
        counts[s[r]] += 1
        swaps = (r-l+1) - max(counts.values())

        while swaps > k:
            counts[s[l]] -= 1
            l += 1
            swaps = (r-l+1) - max(counts.values())

        res = max(res, r-l+1)
        r += 1

    return res

def lrcr():
    print("---lrcr---")
    print(characterReplacement("ABBB", 1))

if __name__ == "__main__":
    lrcr()
    
