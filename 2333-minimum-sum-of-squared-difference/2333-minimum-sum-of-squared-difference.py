class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff=[]
        for i in range(len(nums1)):
            diff.append(abs(nums1[i]-nums2[i]))
        k=k1+k2
        if sum(diff)<=k:
            return 0
        l=0
        h=max(diff)
        while l<h:
            mid=(l+h)//2
            need=0
            for d in diff:
                need+=max(0,d-mid)
            if need<=k:
                h=mid
            else:
                l=mid+1
        r=k
        for i in range(len(diff)):
            r-=max(0,diff[i]-l)
            diff[i]=min(diff[i],l)
        for i in range(len(diff)):
            if r==0:
                break
            if diff[i]==l:
                diff[i]-=1
                r-=1
        a=0
        for d in diff:
            a+=d*d
        return a

        


