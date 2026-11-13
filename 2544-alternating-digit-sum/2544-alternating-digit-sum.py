class Solution(object):
    def alternateDigitSum(self, n):
        c=str(n)
        d=0
        sign=1
        for i in range(len(c)):
            d+=int(c[i])*sign
            sign=sign*-1

        return d

        