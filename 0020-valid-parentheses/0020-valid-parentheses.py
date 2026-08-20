class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        openBrackets = {'(', '{', '['}
        closedBrackets = {'(': ')',
                          '{': '}', 
                          '[': ']'}
        vob = []
        for bracket in s:
            if bracket not in openBrackets:
                if len(vob) == 0 or closedBrackets[vob[-1]] != bracket:
                    return False
                vob.pop()
            else:
                vob.append(bracket)
        if len(vob) == 0:
            return True
        else: 
            return False