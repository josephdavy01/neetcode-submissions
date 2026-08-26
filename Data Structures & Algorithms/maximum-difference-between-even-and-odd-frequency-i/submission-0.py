class Solution:
    def maxDifference(self, s: str) -> int:
        counts = {}

        for char in s:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
        
        max_odd = float('-inf')
        min_even = float('inf')

        for count in counts.values():
            if count % 2 != 0:
                max_odd = max(max_odd,count)
            else:
                min_even = min(min_even,count)

        
        return max_odd - min_even


        
        



