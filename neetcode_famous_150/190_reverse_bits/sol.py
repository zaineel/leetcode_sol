class solution:
    def reverseBits(self, n:int) -> int:
        rev = 0
        for _ in range(32):
            rev = rev << 1
            last = n & 1
            rev = rev | last
            n = n >> 1
        return rev