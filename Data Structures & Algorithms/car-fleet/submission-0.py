class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        # combine the pos & speed lists
        cars = [(p,q) for p, q in zip(position, speed)]
        # sort according to position (decending)
        cars.sort(reverse=True)

        # iterate over cars from closest to farthest
        for car in cars:
            # add the time till target to stack
            time = (target - car[0]) / car[1]
            stack.append(time)

            # if car will reach sooner than car ahead, it joins the prev fleet
            if (len(stack) > 1 and stack[-1] <= stack[-2]):
                stack.pop()
        
        # return the fleets that could not combine
        return len(stack)