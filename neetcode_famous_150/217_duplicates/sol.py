from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        h = {}
        for i in range(len(nums)):
            if(nums[i] in h):
                return True
            h[nums[i]] = i
        return False
    

    def containsDuplicate_2(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
        