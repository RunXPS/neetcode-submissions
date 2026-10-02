import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i = 1
        j = max(piles)
        min_h = j

        while i < j:
            t = 0
            speed = i + (j - i) // 2
            
            for bananas in piles:
                t += math.ceil(float(bananas) / speed)
            if t <= h:
                min_h = min(min_h, speed)

            # print(f"{speed} | {t}")

            if t <= h:
                j = speed
            else:
                i = speed + 1

        return min_h 