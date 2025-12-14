class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        if len(nums) % 2 != 0:
            return False
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
                if freqMap[n] > 2:
                    return False
            else:
                freqMap[n] = 1
        return True
