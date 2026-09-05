class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        consistent_count = 0
        
        for word in words:
            # all() returns True only if every character is in allowed_set
            if all(char in allowed_set for char in word):
                consistent_count += 1
                
        return consistent_count