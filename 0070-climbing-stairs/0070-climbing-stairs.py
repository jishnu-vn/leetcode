class Solution(object):
    def climbStairs(self, n):
        c,p=1,1
        for i in range(1,n):
            c,p=c+p,c
        return c
        