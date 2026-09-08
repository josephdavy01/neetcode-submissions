class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        pref_len = len(pref)

        for i in words:
            # Check if the start of the word matches the prefix
            if i[:pref_len] == pref:
                count += 1

        return count