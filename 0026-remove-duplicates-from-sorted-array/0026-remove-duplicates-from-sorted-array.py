class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        mostRecentNumber = nums[0]

        for i in range(len(nums)):
            if nums[i] != mostRecentNumber:
                nums[j] = nums[i]
                mostRecentNumber = nums[i]
                j += 1
        return j