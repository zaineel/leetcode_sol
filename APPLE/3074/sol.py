class Solution:
    def minimumBoxes(self, apple: list[int], capcity: list[int]) -> int:
        total_apples = sum(apple)
        capcity.sort(key=lambda b:-b)
        boxes = 0
        for size in capcity:
            total_apples -= size
            boxes += 1
            if total_apples <= 0:
                break
        return boxes