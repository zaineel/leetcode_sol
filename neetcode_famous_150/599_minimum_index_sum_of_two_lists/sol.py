class solution:
    def findRestaurents(self, list1: list[str], list2: list[str]) -> list[str]:
        map = {w:i for i, w in enumerate(list1)}
        sum = float('inf')
        res = []
        for j, w in enumerate(list2):
            if w in map:
                idx = j + map[w]
                if idx < sum:
                    sum = idx
                    res = [w]
                elif idx == sum:
                    res.append(w)
        return res