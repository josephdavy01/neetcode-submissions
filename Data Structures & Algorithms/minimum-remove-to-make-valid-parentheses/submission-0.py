class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = list(s)
        balance = 0

        for i, c in enumerate(chars):
            if c == '(':
                balance += 1
            elif c == ')':
                if balance == 0:
                    chars[i] = ''  
                else:
                    balance -= 1

        for i in range(len(chars) - 1, -1, -1):
            if chars[i] == '(' and balance > 0:
                chars[i] = ''
                balance -= 1

        return ''.join(chars)