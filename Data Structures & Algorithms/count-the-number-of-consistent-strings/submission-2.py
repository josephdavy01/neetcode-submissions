class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        consistent_count = 0
        
        for word in words:
            is_consistent = True 
            
            for char in word:
                if char not in allowed:
                    is_consistent = False
                    break 

            if is_consistent:
                consistent_count += 1
                
        return consistent_count