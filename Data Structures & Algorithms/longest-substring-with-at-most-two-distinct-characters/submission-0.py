class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        last_seen = {}
        left = 0
        longest = 0

        for right, char in enumerate(s):
            last_seen[char] = right

            if len(last_seen) > 2:
                # Character with the smallest last-seen index
                leftmost_char = min(last_seen, key=last_seen.get)

                # Move the window past its last occurrence
                left = last_seen[leftmost_char] + 1
                del last_seen[leftmost_char]

            longest = max(longest, right - left + 1)

        return longest