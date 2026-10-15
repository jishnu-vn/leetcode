class Solution(object):
    def sumCounts(self, nums):
        sum=0
        n=len(nums)
        s=[]
        for i in range(n):
            d=[]
            for j in range(i,n):
                d.append(nums[j])
                s.append(d)
                sum+=len(set(d))**2
        return sum
        
