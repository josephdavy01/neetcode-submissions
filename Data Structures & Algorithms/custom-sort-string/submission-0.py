class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Count occurrences of every character in s
        count = [0] * 26

        for ch in s:
            index = ord(ch) - ord('a')
            count[index] += 1

        result = []

        # Add characters according to the custom order
        for ch in order:
            index = ord(ch) - ord('a')

            while count[index] > 0:
                result.append(ch)
                count[index] -= 1

        # Add characters not included in order
        for index in range(26):
            while count[index] > 0:
                result.append(chr(index + ord('a')))
                count[index] -= 1

        return ''.join(result)