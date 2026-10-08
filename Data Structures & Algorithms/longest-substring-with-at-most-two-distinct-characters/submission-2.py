
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        counts = defaultdict(int)
        left = 0
        longest = 0

        for right in range(len(s)):
            counts[s[right]] += 1

            while len(counts) > 2:
                counts[s[left]] -= 1

                if counts[s[left]] == 0:
                    del counts[s[left]]

                left += 1

            longest = max(longest, right - left + 1)
            
        return longest