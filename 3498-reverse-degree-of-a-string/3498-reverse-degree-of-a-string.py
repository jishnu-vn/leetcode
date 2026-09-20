class Solution(object):
    def reverseDegree(self, s):
        answer=0
        for i in range(len(s)):
            answer+=(27-(ord(s[i])%32))*(i+1)
        return answer

        