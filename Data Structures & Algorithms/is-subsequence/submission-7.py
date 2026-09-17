class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ls = list(s)
        lt = list(t)
        la = list()
        for a in lt:
            if a in ls:
                la.append(a)
        i = 0
        while len(ls) < len(la):
            if i == len(ls):
                del la[i:]
                return ls == la
            if ls[i] == la[i]:
                i += 1
                pass
            else:
                la.pop(i)

        return ls == la