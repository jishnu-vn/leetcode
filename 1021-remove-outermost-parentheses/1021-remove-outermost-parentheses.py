class Solution(object):
    def removeOuterParentheses(self, s):
        string=""
        depth=0
        for i in s:
            if i=="(":
                if depth>0:
                    string+=i
                depth+=1
            else:
                depth-=1
                if depth>0:
                    string+=i
        return string

        