class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        fwd = [0] * n
        bwd = [0] * n
        
        fwd[0] = height[0]
        bwd[n-1] = height[n-1]

        water = 0
        for i in range(1,n):
            fwd[i] = max(fwd[i-1], height[i])
            bwd[n-i-1] = max(bwd[(n)-i], height[(n-1) - i])
        
        # hgt: [0,2,0,3,1,0,1,3,2,1]
        # fwd: [0,2,2,3,3,3,3,3,3,3]
        # bwd: [3,3,3,3,3,3,3,3,2,1]
        # wtr:  0+0+2+0+2+3+2+0+0+0 = 9

        # print(fwd)
        # print(bwd)

        for idx in range(n):
            water += min(fwd[idx], bwd[idx]) - height[idx]

        return water
