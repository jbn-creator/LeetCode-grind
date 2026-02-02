class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p = 0
        if s == "":
            return True
        for i in range(len(t)):
            if t[i] == s[p]:
                if p == len(s) - 1:
                    return True
                p += 1
        return False