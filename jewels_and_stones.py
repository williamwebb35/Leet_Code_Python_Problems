class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_l = [i for i in jewels]
        stones_l = [i for i in stones]
        for i in stones_l:
            if i in jewels_l:
                count += 1
        return(count)
