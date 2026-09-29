class Solution(object):
    def sortSentence(self, s):
        words=s.split()
        ans=[""]*len(words)
        for wrd in words:
            ans[int(wrd[-1])-1]=wrd[:-1]
        return " ".join(ans)