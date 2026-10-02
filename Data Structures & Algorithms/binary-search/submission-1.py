class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i: int = 0
        j: int = len(nums)
        c = 0
        while (i < j and c < 10):
            mid: int = i + (j - i) // 2
            if (nums[mid] > target):
                j = mid
            elif (nums[mid] < target):
                i = mid
            else:
                return mid
            c += 1
        return -1