class solution:
    def twoSum(self, nums:list[int], target: int) -> list[int]:
        prev_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in prev_map:
                return [prev_map[diff], i]
            else:
                prev_map[nums[i]] = i
        return []