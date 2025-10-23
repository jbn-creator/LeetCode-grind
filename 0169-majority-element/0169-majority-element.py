class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        for i in range(len(nums)):
            if nums[i] in numsDict:
                numsDict[nums[i]] += 1
            else:
                numsDict[nums[i]] = 1
        maxOccurence = max(numsDict, key=numsDict.get)
        return maxOccurence