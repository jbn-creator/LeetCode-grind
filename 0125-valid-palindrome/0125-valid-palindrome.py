class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        formatedS = "".join(char for char in s if char.isalnum())
        formatedS = formatedS.lower()

        i,j = 0, len(formatedS) - 1
        while i < j:
            if formatedS[i] != formatedS[j]:
                return False
            i += 1
            j -= 1
        return True