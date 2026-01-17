class Solution:
    def climbingStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range(len(n-1)):
            temp = one
            one = one + two
            two = temp
        return one
    
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]