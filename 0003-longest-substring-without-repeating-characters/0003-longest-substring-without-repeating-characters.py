class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        left, answer = 0, 0
        for right in range(len(s)):
            while s[right] in letters:
                letters.remove(s[left])
                left += 1
            letters.add(s[right])
            answer = max(answer, right - left + 1)
        return answer
