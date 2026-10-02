class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # perform a "logical" binary search on the speeds
        l = 1
        r = max(piles)
        min_k = r

        while (l <= r):
            # check new speed
            k = (l + r) // 2

            # calc the total time
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile) / k)

            # update the min_k if less than time
            if totalTime <= h:
                min_k = k
                r = k - 1
            else:
                l = k + 1

        return min_k