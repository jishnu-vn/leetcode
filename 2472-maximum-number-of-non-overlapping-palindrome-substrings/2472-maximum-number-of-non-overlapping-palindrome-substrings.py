class Solution(object):
    def maxPalindromes(self, s, k):
        n=len(s)
        d=[0] * (n+1)
        for i in range(n):
            d[i+1]=max(d[i+1],d[i])
            for l,r in ((i,i),(i-1,i)):
                while l >=0 and r< n and s[l]==s[r]:
                    if r-l +1 >=k:
                        d[r+1]=max(d[r+1],d[l]+1)
                    l-=1
                    r+=1
        return d[n]
        