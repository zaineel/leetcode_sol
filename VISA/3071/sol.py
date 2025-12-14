class Solution:
    def minimumOperationsToWriteY(self, grid: list[list[int]]) -> int:
        n = len(grid)
        mid = n // 2
        cntY = [0, 0, 0]
        cntBg = [0, 0, 0]
        for r in range(n):
            for c in range(n):
                inY = False
                if r <= mid and (c == r or c + r == n - 1):
                    inY = True
                if r >= mid and c == mid:
                    inY = True
                val = grid[r][c]
                if inY:
                    cntY[val] += 1
                    totalY += 1
                else:
                    cntBg += 1
        totalBg = n * n - totalY
        ans = float('inf')

        for yColor in range(3):
            for bgColor in range(3):
                if yColor == bgColor:
                    continue
                yChanges = totalY - cntY[yColor]
                bgChanges = totalBg - cntBg[bgColor]
                ans = min(ans, yChanges + bgChanges)
        return ans