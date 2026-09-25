class Solution(object):
    def findTheDifference(self, s, t):
        soltn=0
        for i in s:
            soltn^=ord(i)
        for i in t:
            soltn^=ord(i)
        return chr(soltn)
        