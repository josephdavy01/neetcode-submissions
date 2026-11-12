class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        
        count = 0
        for w in words:
            is_consistent = True

            for ch in w:
                if ch not in allowed:
                    is_consistent = False
                    break 
                                
            if is_consistent:
                count += 1

        return count