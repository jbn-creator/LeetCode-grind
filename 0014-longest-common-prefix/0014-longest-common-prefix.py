class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        s = sorted(strs)
        result = ""
        for i in range(len(s[0])):
            for word in strs:
                if s[0][i] != word[i]:
                    return result
            result += s[0][i]
        return result

