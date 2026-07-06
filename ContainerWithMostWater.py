class Solution:
    def maxArea(self, height: List[int]) -> int:
    #     #brute force
    #     result = 0
    #     for l in range(height)):
    #         for r in range(l+1, len(height)):
    #             area = (r-l) * min(height[l], height[r])
    #             result = max(res, area)
    #     return result
    
        result = 0
        l, r = 0, len(height) -1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            result = max(result, area)
            if height[l] < height[r]:
                l += 1
            else:
                r-= 1
        return result