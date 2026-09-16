class Solution(object):
    def numberOfSets(self, n, k):
        MOD=1000000007
        dp=[0]*(k+1)
        sum=[0]*(k+1)
        dp[0]=1
        for i in range(1,n):
            for j in range(k,0,-1):
                sum[j]=(sum[j]+dp[j-1])%MOD
                dp[j]=(sum[j]+dp[j])%MOD
        return dp[k]
        