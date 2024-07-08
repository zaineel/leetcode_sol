class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()

        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[i] == '+':
            sign = 1
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        parsed = 0

        while i < len(s):
            curr = s[i]
            if not curr.isdigit():
                break
            else:
                parsed = parsed * 10 + int(curr)

            i += 1
