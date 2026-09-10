class Solution(object):
    def largestAltitude(self, gain):
        alt=0
        maxalt=0
        for diff in gain:
            alt+=diff
            maxalt=max(maxalt,alt)
        return maxalt

        