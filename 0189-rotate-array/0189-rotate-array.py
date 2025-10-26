# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         dictNbr = {}


#         for i in range(len(nums)):
#             newShift = (i - k) % len(nums)
#             if newShift not in dictNbr:
#                 dictNbr[newShift] = {}  # create an empty dictionary first

#         dictNbr[newShift]["original_nbr"] = nums[newShift]

#         for i in range(len(nums)):
#             newShift = (i - k) % len(nums)
#             dictNbr[i]["original_nbr"] = nums[i]

#             dictNbr[newShift]["original_nbr"] = nums[newShift]

#             dictNbr[i]["new_nbr"] = dictNbr[newShift]["original_nbr"]
#             nums[i] = dictNbr[i]["new_nbr"]

#             # nums = [nums.pop()] + nums
#             # print(nums)
        
# -------not my answer

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # handle k > n

        # Reverse the entire array
        nums.reverse()
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
        # Reverse the remaining n-k elements
        nums[k:] = reversed(nums[k:])
