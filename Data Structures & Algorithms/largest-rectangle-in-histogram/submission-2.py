class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rect = 0
        idx = 0

        while idx < len(heights):
            tmp = (idx, -1)
            # while the stack is top is greater than the current
            while len(stack) > 0 and stack[-1][1] > heights[idx]:
                tmp = stack.pop()
                rect = max(rect, (idx - tmp[0]) * tmp[1])

            stack.append((tmp[0], heights[idx]))
            idx += 1
        
        for val in stack:
            rect = max(rect, (idx - val[0]) * val[1])
        
        return rect

        # X | 2
        # 0 | 1
        # X | 5
        # X | 6
        # 1 | 2
        # 2 | 3