class Solution:
    def maximumSubarray(self, nums: list[int]) -> int:
        max_sub = nums[0]
        curSum = 0
        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            max_sub = max(max_sub, curSum)
        return max_sub