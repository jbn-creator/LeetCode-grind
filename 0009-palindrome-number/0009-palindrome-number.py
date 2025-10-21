class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringX = str(x)
        if stringX == stringX[::-1]:
            return True
        return False