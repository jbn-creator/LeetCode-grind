class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        go through the string check the character to see if its part of the set of s1 
        if it is and the length of the substring is = to s1 return True

        if no such substring has been found return False
        
        """
        l, r = 0, len(s1) - 1
        if len(s1) > len(s2):
            return False

        s1Content = {}
        for letter in s1:
            s1Content[letter] = s1Content.get(letter, 0) + 1

        windowContent = {}
        for i in range(len(s1)):
            windowContent[s2[i]] = windowContent.get(s2[i], 0) + 1

        while r < len(s2):
            if windowContent == s1Content:
                return True
            else:
                windowContent[s2[l]] = windowContent.get(s2[l]) - 1
                if windowContent.get(s2[l]) == 0:
                    windowContent.pop(s2[l], None)
                l += 1
                
            r += 1
            if (r < len(s2)):
                windowContent[s2[r]] = windowContent.get(s2[r], 0) + 1            
        return False