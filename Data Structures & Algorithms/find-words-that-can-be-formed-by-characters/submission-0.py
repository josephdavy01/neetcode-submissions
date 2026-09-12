class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total_length = 0
        
        for word in words:
            can_make_word = True
            
            # Check every single letter in the current word
            for letter in word:
                # If the word needs MORE of this letter than what 'chars' has...
                if word.count(letter) > chars.count(letter):
                    can_make_word = False # We can't build it!
                    break # Stop checking this word and move to the next one
            
            # If we checked every letter and didn't run out of pieces
            if can_make_word == True:
                total_length = total_length + len(word)
                
        return total_length