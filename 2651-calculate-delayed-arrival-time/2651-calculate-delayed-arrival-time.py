class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        c=arrivalTime+delayedTime
        return c%24
   