class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        rotated_digits = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        n = len(num)
        l, r = 0, n - 1

        while l <= r:
            if num[l] not in rotated_digits or rotated_digits[num[l]] != num[r]:
                return False

            l += 1
            r -= 1
            
        return True