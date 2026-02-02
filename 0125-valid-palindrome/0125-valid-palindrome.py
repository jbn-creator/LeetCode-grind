# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         answ = True
#         l = 0
#         r = len(s) - 1

#         if len(s) < 2:
#             return True
#         while l <= r:
#             while not s[l].isalnum() and l < r:
#                 l += 1
#             while not s[r].isalnum() and l < r:
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 answ = False
#                 break
#             l += 1
#             r -= 1
#         return answ
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]', '', s)
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True