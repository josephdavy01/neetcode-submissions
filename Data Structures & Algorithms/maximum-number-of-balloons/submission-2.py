class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t = {'b':0,'a':0,'l':0,'l':0,'o':0,'n':0}

        for i in text:
            if i in t:
                t[i] += 1
            else:
                t[i] = 1


        return min(t['b'], t['a'], t['l'] // 2, t['o'] // 2, t['n'])