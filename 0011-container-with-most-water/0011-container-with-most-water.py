class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1 
        maxA = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxA = max(maxA, area)
            print(f"{l} {r} {area}")
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxA

