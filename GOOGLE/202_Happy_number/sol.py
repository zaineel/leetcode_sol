class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = str(n)

        while curr not in seen:
            summ = 0
            seen.add(curr)
            for digit in curr:
                summ += int(digit) ** 2
            if summ == 1:
                return True
            curr = str(summ)
        return False


        