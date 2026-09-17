class Solution(object):
    def minSumOfLengths(self, arr, target):
        n=len(arr)
        INF=float('inf')
        best=[INF]*n
        left=0
        total=0
        shortest=INF
        answer=INF
        for right in range(n):
            total+=arr[right]
            while total>target:
                total-=arr[left]
                left+=1
            if total==target:
                length=right-left+1
                if left>0 and best[left-1]!=INF:
                    answer=min(answer,length+best[left-1])
                shortest=min(length,shortest)
            best[right]=shortest
        if answer==INF:
            return -1
        else:
            return answer
        