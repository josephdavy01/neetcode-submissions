class Solution:
    def largestGoodInteger(self, num: str) -> str:
        string = {}
        for i in num:
            if i in string:
                string[i]+=1
            else:
                string[i]=1
        substring = ""
        max_good = ""
        for digit,count in string.items():
            if count >= 3:
                substring = digit * 3
                if substring in num:
                    max_good = max(max_good,substring)
        
        return max_good



