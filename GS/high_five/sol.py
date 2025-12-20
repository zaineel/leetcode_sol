from collections import defaultdict
import heapq

class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        heaps = defaultdict(list)
        for student_id, score in items:
            heapq.heappush(heaps[student_id], score)
            if len(heaps[student_id]) > 5:
                heapq.heappop(heaps[student_id]) 
        res = []
        for student_id in heaps:
            avg = sum(heaps[student_id]) // 5
            res.append([student_id, avg])
        res.sort(key=lambda x:x[0])
        return res