class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        string = ""
        for i in range(min(len(first),len(last))):
            if first[i] in last[i]:
                string+= first[i]
            else:
                break
        return string

            

