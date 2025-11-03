class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIndex = nums[0]

        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        for i in range(len(nums) - 1):
            if i > maxIndex:
                return False
            maxIndex = max(maxIndex, nums[i] + i)
        if maxIndex < (len(nums) - 1):
            return False
        else:
            return True
    
