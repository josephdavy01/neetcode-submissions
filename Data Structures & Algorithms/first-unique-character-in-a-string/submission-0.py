class Solution:
    def firstUniqChar(self, s: str) -> int:
        char = {}

        for i in s:
            if i in char:
                char[i] += 1
            else:
                char[i] = 1

        for i in range(len(s)):
            if char[s[i]] == 1:
                return i
        
        return -1
        