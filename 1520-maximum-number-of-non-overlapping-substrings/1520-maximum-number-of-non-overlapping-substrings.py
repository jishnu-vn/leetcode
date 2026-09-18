class Solution(object):
    def maxNumOfSubstrings(self, s):
        n=len(s)
        first={}
        last={}
        for i in range(n):
            if s[i] not in first:
                first[s[i]]=i
            last[s[i]]=i
        intervals=[]
        for ch in first:
            start=first[ch]
            end=last[ch]
            valid=True
            i=start
            while i<=end:
                if first[s[i]]<start:
                    valid=False
                    break
                if last[s[i]]>end:
                    end=last[s[i]]
                i+=1
            if valid:
                intervals.append([start,end])
        intervals.sort(key=lambda x:x[1])
        answer=[]
        previous_end=-1
        for start,end in intervals:
            if start>previous_end:
                answer.append(s[start:end+1])
                previous_end=end
        return answer


        