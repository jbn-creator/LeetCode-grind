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
        print(maxIndex)
        print(len(nums) - 1)
        if maxIndex < (len(nums) - 1):
            return False
        else:
            return True
        # i = len(nums) - 2
        # while i >= 0:
        #     if nums[i] == 0:
        #         return False
        #     i -= 1
        # return True

        # for i in range(len(n) - 1)
        # credit = 0
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         credit += 1
        #     else:
        #         if credit < nums[i]:
        #             return False
        #         credit = 0
