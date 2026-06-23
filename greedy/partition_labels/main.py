'''
You are given a string s consisting of lowercase english letters.

We want to split the string into as many substrings as possible, while ensuring that each letter appears in at most one substring.

Return a list of integers representing the size of these substrings in the order they appear in the string.
'''

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        spans = {}

        for i, c in enumerate(s):
            if c in spans:
                spans[c][1] = i
            else:
                spans[c] = [i,i]

        spans_list = list(spans.values())
        res = []
        for span in spans_list:
            print(res)
            if not res:
                res.append(span)

            else:
                coalesced = False
                for j, re in enumerate(res):
                    l, r = span[0], span[1]
                    r_l, r_r  = re[0], re[1]

                    if ( l >= r_l and l <= r_r) or (r >= r_l and r <= r_r ):
                        res[j] = [min(l,r_l), max(r,r_r)]
                        coalesced = True

                if not coalesced:
                    res.append(span)

        ans = []
        for r in res:
            ans.append(r[1] - r[0] + 1)

        return ans

sol = Solution()

s = "xyxxyzbzbbisl"

print(sol.partitionLabels(s))
