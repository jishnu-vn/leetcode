class Solution(object):
    def maxSum(self, nums, k):
        md=10**9+7
        count=[0]*31
        for n in nums:
            for i in range(31):
                if (n >> i)&1:
                    count[i]+=1
        an=0
        for _ in range(k):
            x=0
            for i in range(31):
                if count[i]>0:
                    x|=(1<<i)
                    count[i]-=1
            an=(an+x*x)%md
        return an
        