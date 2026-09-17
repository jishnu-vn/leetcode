class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        return a==a[::-1]