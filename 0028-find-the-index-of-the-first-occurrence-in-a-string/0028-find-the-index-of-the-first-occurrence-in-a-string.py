class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i,j = 0, len(needle)
        # start = 0
        while i < (1 + len(haystack) - len(needle)):
            # KMP attempted - 79 / 85 test cases
            # print(i)
            # while haystack[i + j] == needle[j]:
            #     if j == len(needle) - 1:
            #         return i
            #     j += 1
            # if haystack[i + j] == needle[0]:
            #     i = i + j
            # else:
            #     if start > i:
            #         i = start
            #     else:
            #         i = i + j + 1
            # j = 0
            if haystack[i : j] == needle:
                return i
            else:
                i += 1
                j += 1
        return -1