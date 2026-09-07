class Solution(object):
    def repeatedCharacter(self, s):
        d=[]
        for i in s:
            if i in d:
                return i
            d.append(i)