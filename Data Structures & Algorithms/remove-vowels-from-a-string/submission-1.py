class Solution:
    def removeVowels(self, s: str) -> str:
        v = ""

        for i in s:
            if i not in 'aeiou':
                v += i
                
        return v
