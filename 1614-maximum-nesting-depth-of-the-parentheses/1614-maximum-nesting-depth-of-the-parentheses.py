class Solution(object):
    def maxDepth(self, s):
        count=0
        max=0
        for i in s:
            if i=="(":
                count+=1
                if count>max:
                    max=count
            if i==")":
                count-=1
        return max


        