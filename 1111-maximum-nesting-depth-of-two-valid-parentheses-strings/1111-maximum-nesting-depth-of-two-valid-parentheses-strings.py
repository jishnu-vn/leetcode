class Solution(object):
    def maxDepthAfterSplit(self, seq):
        n=len(seq)
        result=[0]*n
        depth=0
        for i in range(n):
            if seq[i]=="(":
                result[i]=depth%2
                depth+=1
            else:
                depth-=1
                result[i]=depth%2
        return result