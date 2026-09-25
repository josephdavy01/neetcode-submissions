class Solution:
    def reverse(self,l,left,right):
        while left < right:
            l[left],l[right] = l[right],l[left]
            left += 1
            right -= 1

    def reverseWords(self, s: List[str]) -> None:

        self.reverse(s,0,len(s) - 1)
        n = len(s)
        start = 0
        
        while start < n:
            end = start 
            while end < n and s[end] != " ":
                end += 1
            self.reverse(s,start,end-1)
            start = end + 1
        