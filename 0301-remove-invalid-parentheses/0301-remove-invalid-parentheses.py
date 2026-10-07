class Solution(object):
    def removeInvalidParentheses(self, s):
        ans=[]
        def isvalid(s):
            balance=0
            for c in s:
                if c=='(':
                    balance+=1
                elif c==')': 
                    balance-=1
                    if balance<0:
                        return False
            return balance==0
            
        def dfs(s,start,left,right):
            if left==0 and right==0:
                if isvalid(s):
                    ans.append(s)
                return
            for i in range(start,len(s)):
                if i>start and s[i]==s[i-1]:
                    continue
                if left>0 and s[i]=='(':
                    dfs(s[:i]+s[i+1:],i,left-1,right)
                if right>0 and s[i]==')':
                    dfs(s[:i]+s[i+1:],i,left,right-1)
        left=0
        right=0
        for c in s:
            if c=='(':
                left+=1
            elif c==')':
                if left>0:
                    left-=1
                else:
                    right+=1
        dfs(s,0,left,right)
        max_len=max(len(x) for x in ans)
        return[x for x in ans if len(x)==max_len]
                
        