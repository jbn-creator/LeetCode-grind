class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        e = {}
        for i in range(len(nums)):    
            complNumber = target - nums[i] 
            if complNumber in e:            
                index = e[complNumber]
                output =[index, i]
                return output
            e[nums[i]] = i
