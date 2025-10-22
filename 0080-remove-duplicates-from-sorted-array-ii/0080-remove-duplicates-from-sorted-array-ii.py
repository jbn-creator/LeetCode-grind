class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        mostRecentNbr = nums[0]
        NbrOccurence = 1

        if len(nums) == 1:
            return i

        for j in range(1, len(nums)):
            currentNbr = nums[j]
            if currentNbr != mostRecentNbr:
                nums[i] = currentNbr
                i += 1
                mostRecentNbr = currentNbr
                NbrOccurence = 1
            elif NbrOccurence < 2:
                nums[i] = currentNbr
                i += 1
                NbrOccurence += 1
                
        return i

                
                

