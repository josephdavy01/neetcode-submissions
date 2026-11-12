class Solution:
    def longestPalindrome(self, s: str) -> int:
        p = {}

        for i in s:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1

        t = 0
        odd = False

        for v in p.values():
            if v % 2 == 0:
                t += v
            else:
                t += v - 1
                odd = True
        
        if odd:
            t += 1
        return t
