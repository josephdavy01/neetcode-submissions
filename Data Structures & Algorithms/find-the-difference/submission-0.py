class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        p = {}

        for i in t:
            if i in p:
                p[i] += 1
            else:
                p[i] = 1
        
        for i in s:
            p[i] -= 1
        
        for char,count in p.items():
            if count == 1:
                return char



        