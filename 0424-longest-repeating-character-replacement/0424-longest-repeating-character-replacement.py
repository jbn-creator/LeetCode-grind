class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        while right pointer is in s
            if the number of diverging character is less than k keep increasing the substring size
            else increase your left pointer and decrease the length of the substring
         
        how do i determine the number of diverging character in a substring ? cardinality of a set - len of the string
        """
        freq = {}
        l = 0
        ans = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while ((r - l + 1) - max(freq.values())) > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans