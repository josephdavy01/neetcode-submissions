class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Define the valid upside-down pairs
        rotated_digits = {
            '0': '0', '1': '1', '6': '9', '8': '8', '9': '6'
        }
        
        n = len(num)
        # Place pointers at the beginning (left) and end (right)
        l, r = 0, n - 1
        
        # Move inward until the pointers cross
        while l <= r:
            # If the left digit can't be flipped, OR 
            # if the flipped left digit doesn't match the right digit
            if num[l] not in rotated_digits or rotated_digits[num[l]] != num[r]:
                return False
            
            # Move the fingers one step closer to the middle
            l += 1
            r -= 1
            
        # If we made it through the whole string, it's valid
        return True