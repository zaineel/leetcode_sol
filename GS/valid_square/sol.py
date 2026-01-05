from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(a: List[int], b: List[int]) -> int:
            return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
        points = [p1, p2, p3, p4]
        distances = []

        for i in range(4):
            for j in range(i+1, 4):
                distances.append(distance(points[i], points[j]))
        if distances[0] == 0 or len(set(distances)) != 2:
            return False
        distances.sort()
        side = distances[0]
        diagonal = distances[-1]
        if distances.count(side) != 4 or distances.count(diagonal) != 2:
            return False
        return diagonal == 2 * side 