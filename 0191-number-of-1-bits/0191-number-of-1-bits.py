class Solution(object):
    def hammingWeight(self, n):
        c=0
        while n:
            c+=n%2
            n//=2
        return c

        