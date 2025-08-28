class solution:
    def topkfrequent(self, nums: list[int], k: int) -> list[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        sorted_pairs = sorted(hash_map.items(), lambda x: x[1], reverse = True)
        res = []
        for num, freq in sorted_pairs:
            if len(res) < k:
                res.append(num)
            else:
                break
        return res

