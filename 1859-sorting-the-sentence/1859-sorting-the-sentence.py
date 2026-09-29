class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        ans=[""]*len(words)
        for wrd in words:
            place=int(wrd[-1])-1
            ans[place]=wrd[:-1]
        return " ".join(ans)