class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answ = 0
        lenSubs = 1
        if len(s) == 1:
            return 1
        if len(s) == 0:
            return 0
        l,r = 0, 1
        seenChar = {s[l]}
        while r < len(s):
            if s[r] not in seenChar:
                lenSubs += 1
                seenChar.add(s[r])
                r += 1
            else:
                seenChar.remove(s[l])
                l += 1
                lenSubs -= 1
            answ = max(answ, lenSubs)
        return answ