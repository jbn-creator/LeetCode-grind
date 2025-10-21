class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
       j, k =  1, 1
       lastDifferentNumber = nums[0]
       for i in range(len(nums)):
           if nums[i] != lastDifferentNumber:
               nums[j] = nums[i]
               lastDifferentNumber = nums[i]
               k += 1
               j += 1
       return k
