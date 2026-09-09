class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        jwel=set(jewels)
        for i in stones:
            if i in jwel:
                count+=1
        return count

        