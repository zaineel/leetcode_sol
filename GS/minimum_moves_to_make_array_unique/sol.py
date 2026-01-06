from collections import defaultdict


class Solution:
    def minMoves(self, nums: list[int]) -> int:
        count = defaultdict(int)
        moves = 0
        for num in nums:
            count[num] += 1
        for i in range(len(nums) + max(nums)):
            if count[i] > 1:
                extra = count[i] - 1
                count[i+1] += extra
                count[i] = 1
                moves += extra
        return moves