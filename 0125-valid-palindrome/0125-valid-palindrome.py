class Solution:
    def isPalindrome(self, s: str) -> bool:
        answ = True
        l = 0
        r = len(s) - 1

        if len(s) < 2:
            return True
        while l <= r:
            while not s[l].isalnum() and l < r:
                l += 1
            while not s[r].isalnum() and l < r:
                r -= 1
            if s[l].lower() != s[r].lower():
                answ = False
                break
            l += 1
            r -= 1
        return answ