class solution:
    def longestSubstring(self, nums: list[int]) -> int:
        longest = 0
        s = set(nums)
        for num in s:
            if (num - 1) not in s:
                length = 1
                while (num + length) in s:
                    length += 1
                longest = max(longest, length)
        return longest