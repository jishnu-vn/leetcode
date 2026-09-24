class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            num=nums[i]
            sum=0
            while num>0:
                digit=num%10
                sum+=digit
                num=num//10
            if sum==i:
                return i
        else:
            return -1
        