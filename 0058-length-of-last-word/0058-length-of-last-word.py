class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lastWordLength = 0
        lastChar = ' '
        for i in range(len(s)):
            if lastChar == ' ' and s[i] != ' ':
                lastWordLength = 1
            elif s[i] != ' ':
                lastWordLength += 1
            lastChar = s[i]

        return lastWordLength