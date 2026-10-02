class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        
        for idx in range(len(heights)):
            tmp = (idx, -1)

            while (len(stack) > 0 and heights[idx] < stack[-1][1]):
                tmp = stack.pop()
                area = max(area, (idx - tmp[0])*tmp[1])
            
            stack.append((tmp[0], heights[idx]))

        for pair in stack:
            area = max(area, (len(heights) - pair[0]) * pair[1])

        return area