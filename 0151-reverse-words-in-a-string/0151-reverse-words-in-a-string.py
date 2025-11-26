class Solution:
    def reverseWords(self, s: str) -> str:
        answ = ""
        lastWord = ""
        for i in range(len(s)):
            if s[i] != " ":
                if answ != "" and lastWord == "":
                    answ = " " + answ
                lastWord += s[i]
            else:
                answ = lastWord + answ
                lastWord = ""
        answ = lastWord + answ
        return answ
            