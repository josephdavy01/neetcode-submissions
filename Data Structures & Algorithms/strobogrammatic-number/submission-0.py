class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        rotated = []
        
        for char in reversed(num):
            if char not in pairs:
                return False
            rotated.append(pairs[char])
            
        return "".join(rotated) == num