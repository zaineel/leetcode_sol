class Solution: 
    def maxDistance(self, colors: list[int]) -> int: 
        max_dist = 0 
        n = len(colors) 
        for i in range(n): 
            if colors[i] != colors[0]: 
                max_dist = max(max_dist, i - 0) 
            if colors[i] != colors[n - 1]: 
                max_dist = max(max_dist, n - 1 - i) 
        return max_dist