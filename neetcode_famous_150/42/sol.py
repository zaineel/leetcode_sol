class solution:
    def TrapWater(self, height: list[int]) -> int:
        total = 0
        if not height:
            return 0
        l, r = 0, (len(height) - 1)
        leftMax = height[l]
        rightMax = height[r]
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                total += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                total += rightMax - height[r]
        return total