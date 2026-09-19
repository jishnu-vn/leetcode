class Solution(object):
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        closex=max(x1,min(xCenter,x2))
        closey=max(y1,min(yCenter,y2))
        xdistance=xCenter-closex
        ydistance=yCenter-closey
        distancesqr=xdistance**2+ydistance**2
        return distancesqr<=radius**2