class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        c=arrivalTime+delayedTime
        if c==24:
            return 0
        if c<=24:
            return c
        else:
            return abs(24-c)
   