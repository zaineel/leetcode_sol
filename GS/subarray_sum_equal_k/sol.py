from collections import defaultdict


class Solution:
    def subArraySum(self, nums: list[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0                       # ans
        prefix = 0                      # running total

        for num in nums:
            prefix += num
            count += freq[prefix - k]   # imp line 
            freq[prefix] += 1

        return count