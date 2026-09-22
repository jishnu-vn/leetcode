class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        c=0
        d=sentence.split()
        lenwrd=len(searchWord)
        for i in range(len(d)):
            if d[i].startswith(searchWord):
                return i+1
        return -1