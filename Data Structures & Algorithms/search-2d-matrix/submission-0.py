class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m: int = len(matrix) # 3
        n: int = len(matrix[0]) # 4
        i = 0 # 5
        j = m * n # 6
        
        while (i < j):
            mid = i + (j - i) // 2 # 5
            row = mid // n # 5
            col = mid % n # 1

            # print(f"{i} | {j}")
            if (matrix[row][col] > target):
                j = mid
            elif (matrix[row][col] < target):
                i = mid + 1
            else:
                return True
        return False

        # 11 -> 4 -> 8 -> 10
        # 12 -> 8 -> 11 -> 10