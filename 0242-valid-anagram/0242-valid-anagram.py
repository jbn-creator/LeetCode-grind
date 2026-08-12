from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        C1 = Counter(s)
        C2 = Counter(t)
        if C1 == C2:
            return True
        return False
        