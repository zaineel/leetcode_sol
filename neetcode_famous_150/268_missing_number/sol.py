class Solutiion:
    def missingNumber(self, nums: list[int]) -> int:
        sum = len(nums) * len(nums) + 1 // 2
        for num in nums:
            sum -= num
        return sum

