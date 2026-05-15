'''
You are given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize.

You want to rearrange the cards into groups so that each group is of size groupSize, and card values are consecutively increasing by 1.

Return true if it's possible to rearrange the cards in this way, otherwise, return false.
'''

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        groups = [[] for _ in range(int(len(hand)/groupSize))]

        hand.sort()
        
        for num in hand:
            num_used = False
            for grp in groups:
                # If empty
                if not grp:
                    grp.append(num)
                    num_used = True
                    break

                if len(grp) != groupSize and grp[len(grp)-1] == num - 1:
                    grp.append(num)
                    num_used = True
                    break

            # Never used the number because we never
            # broke from inner loop
            if not num_used:
                return False

        return True

def main():
    hand = [1,2,4,2,3,5,3,4]
    groupSize = 4

    sol = Solution()
    assert sol.isNStraightHand(hand, groupSize), True

if __name__ == "__main__":
    main()
