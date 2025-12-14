class Solution:
    def oddString(self, words: list[str]) -> str:
        def pattern(w):
            return tuple(ord(w[j]) - ord(w[j-1]) for j in range(1, len(w)))
        p0 = pattern(words[0])
        p1 = pattern(words[1])
        p2 = pattern(words[2])
        if p0 == p1:
            common = p0
        elif p0 == p2:
            common = p0
        else:
            common = p1
        for i in range(len(words)):
            if common != pattern(words[i]):
                return words[i]