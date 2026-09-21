class Solution(object):
    def resultArray(self, nums, k):
        ans=[0]*k
        dp=[0]*k
        for num in nums:
            newdp=[0]*k
            nummod=num%k
            newdp[nummod]=1
            for i in range(k):
                newmod=(i*nummod)%k
                newdp[newmod]+=dp[i]
            for i in range(k):
                ans[i]+=newdp[i]
                dp=newdp
        return ans

        
        