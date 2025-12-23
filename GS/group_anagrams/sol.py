from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        freq = defaultdict(list)
        for st in strs:
            count = [0] * 26
            for char in st:
                count[ord(char) - ord('a')] += 1
            freq[tuple(count)].append(st)
        return list(freq.values())