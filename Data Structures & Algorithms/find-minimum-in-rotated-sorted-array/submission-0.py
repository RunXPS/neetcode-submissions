class Solution:
    def findMin(self, nums: List[int]) -> int:
        i: int = 0 # 4
        j: int = len(nums) # 6
        first: int = nums[0] # 3

        while (i < j):
            mid = i + (j - i) // 2 # 5
            first = min(first, nums[mid])
            # in upper rot
            if (nums[mid] > first):
                i = mid + 1
            # elif (nums[mid] < first):
            else:
                j = mid
            # else:
            #     return nums[mid]
        
        return first