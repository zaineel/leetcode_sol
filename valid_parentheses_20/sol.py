class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = [] #python list
        closeToOpen = {')' : '(', ']' : '[', '}' : '{'} # hash map

        for c in s:
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

