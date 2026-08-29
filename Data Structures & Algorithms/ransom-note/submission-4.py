class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        
        for char in magazine:
            if char in mag_letters:
                mag_letters[char] += 1
            else:
                mag_letters[char] = 1
                
        for char in ransomNote:
            if char not in mag_letters or mag_letters[char] == 0:
                return False
            
            mag_letters[char] -= 1
            
        return True