class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1
        while l < r:
            if height[l] < height[r]:
                max_water = max(max_water, l * (r-l))
                l += 1
            else:
                max_water = max(max_water, r * (l-r))
                r -= 1
        return max_water