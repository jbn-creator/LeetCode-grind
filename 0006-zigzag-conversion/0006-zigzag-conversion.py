class Solution:
    def convert(self, s: str, numRows: int) -> str:
        vals = ""
        if numRows == 1:
            return s
        for i in range(numRows):
            j = i
            edgeCase = False 
            while j < len(s):
                vals += s[j]
                if i == 0 or (i == numRows - 1):
                    j += (numRows - 1) * 2
                else:
                    if edgeCase:
                        j += 2 * i
                    else:
                        j += 2 * (numRows - i - 1) 
                edgeCase = not edgeCase
        return vals