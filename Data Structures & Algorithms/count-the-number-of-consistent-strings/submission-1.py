class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0
        
        # Check one word at a time
        for word in words:
            # Assume the word is consistent until we find a rule-breaking letter
            is_consistent = True 
            
            # Check each letter in the current word
            for char in word:
                # If the letter is NOT in our allowed list, flag it and stop checking
                if char not in allowed:
                    is_consistent = False
                    break 
                    
            # If we checked every letter and the flag is still True, count it
            if is_consistent:
                consistent_count += 1
                
        return consistent_count