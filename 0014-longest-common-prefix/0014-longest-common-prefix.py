class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(len(strs[0]))
        val = ""
        minW = min(strs)
        i = 0
        while i < len(minW):
            for j in range(len(strs)):
                if strs[j][i] != minW[i]:
                    
                    return val
            val += minW[i]
            i += 1
        return val
                

