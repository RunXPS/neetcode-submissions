import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        curr_max = j
        while i <= j:
            mid = (i + j) // 2
            hours = 0
            for b in piles:
                hours += math.ceil(b / mid)
            if hours <= h:
                curr_max = mid
                j = mid - 1
            else:
                i = mid + 1

        return curr_max

        # 0 - 4 | 2 | 6