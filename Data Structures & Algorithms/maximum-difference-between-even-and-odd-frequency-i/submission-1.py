class Solution:
    def maxDifference(self, s: str) -> int:
        c = {}

        for i in s:
            if i in c:
                c[i] += 1
            else:
                c[i] = 1

        o = float('-inf')
        e = float('inf')

        for i in c.values():
            if i % 2 == 0:
                e = min(e,i)
            else:
                o = max(o,i)

        return o - e
