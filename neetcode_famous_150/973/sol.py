import heapq
class Solution:
    def KClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        res = []
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        while k > 0:
            dist, x , y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res