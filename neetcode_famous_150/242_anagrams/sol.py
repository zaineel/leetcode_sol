class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return (sorted(s) == sorted(t))

    
        # count_s, count_t = {}, {}
        # for i in range(len(s)):
        #     count_s[s[i]] = 1 + count_s.get(s[i], 0)
        #     count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # for c in count_s:
        #     if (count_s[c] != count_t.get(c, 0)):
        #         return False
        # return True