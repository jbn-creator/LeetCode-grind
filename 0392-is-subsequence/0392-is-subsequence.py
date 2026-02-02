class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p , q = 0 , 0
        if s == "":
            return True
        while q < len(t):
            if s[p] == t[q]:
                if p == len(s) - 1:
                    return True
                else:
                    p += 1
            q += 1
        return False