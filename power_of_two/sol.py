class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        num = math.log(n,2)
        ans = abs(num - round(num)) < 1e-10 
        if(ans):
            return True
        else:
            return False