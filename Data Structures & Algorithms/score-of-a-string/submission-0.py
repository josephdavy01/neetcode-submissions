class Solution:
    def scoreOfString(self, s: str) -> int:
        Sum = 0
        for i in range(len(s)-1):
            diff = abs(ord(s[i]) - ord(s[i+1]))
            Sum += diff 
        
        return Sum



        