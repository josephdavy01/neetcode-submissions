class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        p = {}

        for i in s:
            if i in p:
                p[i]+=1
            else:
                p[i] = 1

        odd = 0

        for i in p.values():
            if i % 2 != 0:
                odd += 1
        
        if odd <= 1:
            return True
        else:
            return False
        
        


        