class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        def atMostKDistinct(k):
            counts = {}
            left = 0
            longest = 0

            for right in range(len(s)):
                counts[s[right]] = counts.get(s[right], 0) + 1

                while len(counts) > k:
                    counts[s[left]] -= 1
                    if counts[s[left]] == 0:
                        del counts[s[left]]
                    left += 1

                longest = max(longest, right - left + 1)

            return longest

        return atMostKDistinct(2)