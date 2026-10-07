class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        k = 0

        while i < n:
            ch = chars[i]

            j = i
            while j < n and chars[j] == ch:
                j += 1
            
            count = j - i

            chars[k] = ch 
            k += 1

            if count > 1:
                for digit in str(count):
                    chars[k] = digit
                    k += 1
            
            i = j 

        return k


        