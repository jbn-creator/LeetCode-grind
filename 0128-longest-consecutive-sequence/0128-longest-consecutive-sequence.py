class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        sortedNums = sorted(nums)
        count = 1
        maxCount = count
        for i in range(1, len(sortedNums)):
            if (sortedNums[i] - 1) == sortedNums[i - 1]:
                count += 1
            elif sortedNums[i] == sortedNums[i - 1]:
                continue 
            else: 
                maxCount = max(count, maxCount)
                count = 1
        return max(count, maxCount)
