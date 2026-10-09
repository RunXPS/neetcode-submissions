class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashset = set(nums)
        out = []


        for i in range(1, len(nums) + 1):
            if not (i in hashset):
                out.append(i)
        
        return out